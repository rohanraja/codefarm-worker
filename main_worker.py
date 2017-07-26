import os, sys
from initcmds import *

from machineHelpers import *
from filetransfers import getLocalImagesList

def init():
    myIp = getLocalIP()
    images = getLocalImagesList()
    initWorker(myIp, images)




cmdDict = {
        "init": init,
}


cmdDict[sys.argv[1]]()
