import os, sys
from initcmds import *

from machineHelpers import *

def initRepo():
    myIp = getLocalIP()
    projInfo = getProjInfo()
    wid = initDev(myIp, projInfo)
    setWorkspaceId(str(wid))


def build():

    branch = getWorkingBranch()
    wid = getWorkspaceId()
    requestBuild(wid, branch)



cmdDict = {
        "initRepo": initRepo,
        "build": build
}


cmdDict[sys.argv[1]]()
