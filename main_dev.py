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
    sid = requestBuild(wid, branch)
    setActiveSession(sid)


def printStats(stats):
    for st in stats:
        print "%s\n" % st

def status():
    sid = getActiveSession()
    stats = getSessionStats(sid)
    printStats(stats)


cmdDict = {
        "initRepo": initRepo,
        "build": build,
        "status": status,
}


if __name__ == "__main__":
    cmdDict[sys.argv[1]]()
