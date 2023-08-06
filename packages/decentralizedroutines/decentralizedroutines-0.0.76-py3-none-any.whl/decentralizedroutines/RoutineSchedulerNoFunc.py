
from dataclasses import dataclass
import os,glob,subprocess,pytz
from threading import local
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timezone, tzinfo
from tzlocal import get_localzone 

from SharedData.Logger import Logger
logger = Logger(__file__)

from SharedData.SharedDataAWSKinesis import KinesisLogStreamConsumer,KinesisStreamProducer
consumer = KinesisLogStreamConsumer()

stream_name='deepportfolio-workerpool'
profile_name='master'
producer = KinesisStreamProducer(stream_name, profile_name)

# LoadSchedule
if not 'SCHEDULE_PATH' in os.environ:
    raise Exception('SCHEDULE_PATH not found in environ!')
else:
    schedpath = Path(os.environ['SCHEDULE_PATH'])

local_tz = pytz.timezone(str(get_localzone()))
today = datetime.now().date()
year = today.timetuple()[0]
month = today.timetuple()[1]
day = today.timetuple()[2]        

_sched = pd.read_excel(schedpath)
sched = pd.DataFrame()
for i,s in _sched.iterrows():
    runtimes = s['Run Times'].split(',')
    for t in runtimes:
        hour = int(t.split(':')[0])
        minute = int(t.split(':')[1])
        dttm = local_tz.localize(datetime(year,month,day,hour,minute))
        s['Run Times'] = dttm
        sched = sched.append(s)       

sched = sched.sort_values(by=['Run Times','Name','Computer']).reset_index(drop=True)
sched['Status'] = np.nan
sched['Last Message'] = np.nan

# RefreshLogs
dflogs = consumer.readLogs()
if not dflogs.empty:
    dflogs = dflogs[dflogs['asctime'].notnull()].copy()
    dflogs['asctime'] = pd.to_datetime(dflogs['asctime'])
    dflogs['asctime'] = [dt.astimezone(tz=local_tz) for dt in dflogs['asctime']]

    i=0
    for i in sched.index:
        r = sched.loc[i]
        idx = dflogs['logger_name']==r['Script']
        idx = (idx) & (dflogs['user_name']==r['Computer'])
        idx = (idx) & (dflogs['asctime']>=r['Run Times'])    
        if np.any(idx):    
            sched.loc[i,'Last Message'] = dflogs[idx].iloc[-1]['message']   

                        
    dferr = dflogs[dflogs['message']=='ROUTINE ERROR!']
    dferr = dferr.reset_index(drop=True).sort_values(by='asctime')
    i=0
    for i in dferr.index:
        r = dferr.iloc[i]
        idx = sched['Script']==r['logger_name']
        idx = (idx) & (sched['Computer']==r['user_name'])
        idx = (idx) & (r['asctime']>=sched['Run Times'])
        if idx.any():
            ids = idx[::-1].idxmax()
            sched.loc[ids,'Status'] = 'ERROR'
            idx = sched.loc[idx,'Status'].isnull()
            idx = idx.index[idx]
            sched.loc[idx,'Status'] = 'EXPIRED'

    compl = dflogs[dflogs['message']=='ROUTINE COMPLETED!'].reset_index(drop=True).sort_values(by='asctime')
    i=0
    for i in compl.index:
        r = compl.iloc[i]
        idx = sched['Script']==r['logger_name']
        idx = (idx) & (sched['Computer']==r['user_name'])
        idx = (idx) & (r['asctime']>=sched['Run Times'])
        if idx.any():
            ids = idx[::-1].idxmax()
            sched.loc[ids,'Status'] = 'COMPLETED'
            idx = sched.loc[idx,'Status'].isnull()
            idx = idx.index[idx]
            sched.loc[idx,'Status'] = 'EXPIRED'

sched

#getPendingRoutines
idx = sched['Status'].isnull()
idx = (idx) & (sched['Run Times']<=datetime.now().astimezone(tz=local_tz))
dfpending = sched[idx]
i=1
for i in dfpending.index:
    r = dfpending.loc[i]    
    if not str(r['Dependencies'])=='nan':
        run=True
        dependencies = r['Dependencies'].replace('\n','').split(',')
        dep=dependencies[0]
        for dep in dependencies:
            computer = dep.split(':')[0]
            script = dep.split(':')[1]
            idx = sched['Computer']==computer
            idx = (idx) & (sched['Script']==script)
            idx = (idx) & (sched['Run Times']<=datetime.now().astimezone(tz=local_tz))
            ids = sched.index[idx]
            if len(ids)==0:
                Logger.log.error('Dependency not scheduled for '+r['Computer']+':'+r['Script'])
            else:
                if not str(sched.loc[ids[0],'Status']) == 'COMPLETED':
                    run=False
        if run:
            sched.loc[i,'Status'] = 'PENDING'
    else:
        sched.loc[i,'Status'] = 'PENDING'

sched

# Run pending routines
dfpending = sched[sched['Status']=='PENDING']
for i in dfpending.index:
    r = dfpending.loc[i]
    target = r['Computer']    
    repo = r['Script'].split('\\')[0]
    routine = r['Script'].replace(repo,'')[1:]+'.py'
    data = {
        "sender" : "MASTER",
        "job" : "routine",
        "target" : target,        
        "repo" : repo,
        "routine" : routine
    }
    producer.produce(data,'command')
    sched.loc[r.name,'Status'] = 'RUNNING'

sched