import urllib
import config

import glob, os

def getOutputPath(imName):
    return "%s/images/%s.tar" % (config.WORK_DIR , imName)


def requestImageFromServer(imageUrl, imageName):
    path = getOutputPath(imageName)
    if(os.path.exists(path)):
        return path

    urllib.urlretrieve (imageUrl, path)
    return path


def getLocalImagesList():
    path = "%s/images/*.tar" % (config.WORK_DIR)
    outList = []
    for filee in glob.glob(path):
        filee = filee.split("/")[-1]
        outList.append(filee.replace(".tar", ""))
    return outList


#### ### ## FILE SERVER #### ### ##


import os
import threading


def blockingServer():

    cmd = ("cd %s/images; python -m SimpleHTTPServer" % (config.WORK_DIR))
    os.system(cmd)

def hostImageFile():

    threading.Thread(target=blockingServer).start()
