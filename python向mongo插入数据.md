# blog


```python

#! /usr/bin/env python
#coding=utf-8

import random
import datetime,time
import pymongo


SOURCEID = ["91","360","IOS","BW"]
SERVERID = [1,2,3,4]
ACCOUNT = ["1234","BNN43","MNJJD"]
EVENTNAME = ["login","buyItem","pvp"]
GOLD = [50,60,70,15]
TIME = [1,2,3,4,5]
ROLEID = ["1","2","3","4","5","6"]




def putDatas():
    """
    """
    db = pymongo.Connection("192.168.1.2")["mean-dev"]
    for i in range(1000):
        datas = {}
        datas["sourceID"] = random.choice(SOURCEID)
        datas["serverID"] = random.choice(SERVERID)
        datas["account"] = random.choice(ACCOUNT)
        datas["name"] = "blingbling"
        datas["roleID"] = random.choice(ROLEID)
        datas["eventName"] = random.choice(EVENTNAME)
        datas["createdTime"] = time.time() - (random.choice(TIME)*60*60*24)
        datas["result"] = True
        datas["gold"] = random.choice(GOLD)
        __put(db,datas)
        print datas


def __put(db,datas):
    #db["test"].update({"createdTime":datas["createdTime"]},datas,upsert=True)
    db["logs"].insert(datas)



putDatas()

```

