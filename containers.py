from dockerapi import *
from sessionsManager import *
import statuses as st


def getExposedPorts(r):

    outP = {}
    c = getContainer(r)
    
    if c == None :
        return outP

    for port in r["ports"]:
        hostPrt = findHostPort(c.id, port)
        outP[port] = hostPrt

    return outP

def checkAndStopExistingContainer(r):
    c = getContainer(r)
    if c != None:
        c.stop()

def checkAndDownloadImage(r):

    if imageExists(r["image"]):
        updateStatus(r, st.IM_EXISTS) 
        return
    updateStatus(r, st.IM_DOWNLOAD) 
    downloadImage(r)


def setupContainer(r):

    r["fromPath"] = r["localClonedPath"]
    r["toPath"] = r["srcPath"]

    checkAndDownloadImage(r)
    checkAndStopExistingContainer(r)

    updateStatus(r, st.INIT_DOCKER) 
    c = dockerRun(r)
    addContainer(r,c)

    #startContainerMonitor()

