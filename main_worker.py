import os, sys
from initcmds import *

from machineHelpers import *
from filetransfers import getLocalImagesList
from requestListener import runRequestLooper

def init():
    myIp = getLocalIP()
    images = getLocalImagesList()
    initWorker(myIp, images)


def runDaemon():
    
    myIp = getLocalIP()
    runRequestLooper(myIp)


cmdDict = {
        "init": init,
        "run": runDaemon,
}


cmdDict[sys.argv[1]]()
