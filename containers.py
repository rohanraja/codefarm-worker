from dockerapi import *
from sessionsManager import *
import statuses as st
from machineHelpers import getLocalIP


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

def updateExposedPortsStatus(r):

    myIp = getLocalIP()
    outStat = ""

    ports = getExposedPorts(r)
    for p in ports:
        outStat = outStat + "Port %s -> http://%s:%s\n" % (p, myIp, ports[p])

    updateStatus(r, outStat.rstrip())

def setupContainer(r):

    r["fromPath"] = r["localClonedPath"]
    r["toPath"] = r["srcPath"]

    checkAndDownloadImage(r)
    checkAndStopExistingContainer(r)

    updateStatus(r, st.INIT_DOCKER) 
    c = dockerRun(r)
    addContainer(r,c)

    updateExposedPortsStatus(r)

    #startContainerMonitor()

