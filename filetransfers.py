import urllib
import config


def getOutputPath(imName):
    return "%s/images/%s" % (config.WORK_DIR , imName)


def requestImageFromServer(imageUrl, imageName):
    path = getOutputPath(imageName)
    urllib.urlretrieve (imageUrl, path)
    return path


#### ### ## FILE SERVER #### ### ##


import os
import threading


def blockingServer():

    cmd = ("cd %s/images; python -m SimpleHTTPServer" % (config.WORK_DIR))
    os.system(cmd)

def hostImageFile():

    threading.Thread(target=blockingServer).start()
