import os, sys
from initcmds import *

from machineHelpers import *
from filetransfers import getLocalImagesList, hostImageFile
from requestListener import runRequestLooper

def init():
    myIp = getLocalIP()
    images = getLocalImagesList()
    initWorker(myIp, images)


def runDaemon():
    
    myIp = getLocalIP()
    runRequestLooper(myIp)
    hostImageFile()


cmdDict = {
        "init": init,
        "run": runDaemon,
}


if __name__ == "__main__":
    cmdDict[sys.argv[1]]()
