import os, sys
from initcmds import *

from machineHelpers import *

cmdDict = {
        "initRepo": initRepo
}

def initRepo():
    myIp = getLocalIP()
    projInfo = getProjInfo()
    initDev(myIp, projInfo)





cmdDict[sys.argv[1]]()
