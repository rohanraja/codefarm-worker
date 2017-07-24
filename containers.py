from dockerapi import *

containersDict = {}

def addContainer(r, c):
    containersDict[r["sessionId"]] = c

def getExposedPorts(sid):

    if containersDict.contains_key(sid):
        c = containersDict[sid]
        return c.ports()

    return ""

def checkAndStopExistingContainer(sid):

    if containersDict.contains_key(sid):
        c = containersDict[sid]
        c.stop()

def checkAndDownloadImage(r):

    if imageExists(r["image"]):
        return
    downloadImage(r)


def setupContainer(r):

    r["fromPath"] = r["localClonedPath"]
    r["toPath"] = r["srcPath"]

    checkAndDownloadImage(r)
    checkAndStopExistingContainer(r["sessionId"])
    c = dockerRun(r)
    addContainer(r,c)

