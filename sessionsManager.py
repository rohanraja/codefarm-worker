import statuses as st
import json
import time
import config
import threading
from servercomm import *
from initcmds import statuses

statusDict = {}
containersDict = {}


def getStatus(r):
    if r["sessionId"] in statusDict:
        return statusDict[r["sessionId"]]
    return []

def updateStatus(r, status):
    statList = getStatus(r)
    statList.append(status)
    statusDict[r["sessionId"]] = statList

def addContainer(r, c):
    containersDict[r["sessionId"]] = c

def getContainer(r):
    if r["sessionId"] in containersDict:
        return containersDict[r["sessionId"]]
    return None


def sendStatusDictToServer(stadict, wid):
    statuses.merge(stadict)



IsStatusUpdateRunning = False

def blockingStatusDispatcher(workerId):

    global IsStatusUpdateRunning

    IsStatusUpdateRunning = True

    while True:
        time.sleep(config.STATUS_INTERVAL)
        if len(statusDict.keys()) == 0:
            continue
        sendStatusDictToServer(statusDict, workerId)

    IsStatusUpdateRunning = False

def invokeStatusDispatcher(workerId):
    if IsStatusUpdateRunning == False:
        threading.Thread(target=blockingStatusDispatcher, args=(workerId,)).start()

