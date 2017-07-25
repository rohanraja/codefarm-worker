from dockerapi import *

containersDict = {}

def addContainer(r, c):
    containersDict[r["sessionId"]] = c

def getContainer(r):
    if r["sessionId"] in containersDict:
        return containersDict[r["sessionId"]]
    return None

def getExposedPorts(r):

    outP = {}
    c = getContainer(r)

    for port in r["ports"]:
        hostPrt = findHostPort(c.id, port)
        outP[port] = hostPrt

    return outP

def checkAndStopExistingContainer(sid):

    if sid in containersDict:
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

