from gitapi import *
import os
import config
from containers import *
from sessionsManager import *
import statuses as st
import machineHelpers

def getCloneDir(r):

    outp = os.path.join(config.WORK_DIR, r["sessionId"])
    return outp


def processBuildRequest(r):

    print "Processing Build Request %s" % r

    updateStatus(r, st.BUILDREQUEST)
    invokeStatusDispatcher(machineHelpers.getLocalIP())

    outPath = getCloneDir(r)
    if(os.path.exists(outPath)):
        updateStatus(r, st.PULLINGBRANCH%(r["branchName"])) 
        try:
            pullBranch(outPath)
        except:
            pass
    else:
        updateStatus(r, st.CLONING%(r["branchName"], r["repoUrl"])) 
        cloneBranch(r["repoUrl"], r["branchName"], outPath)
    r["localClonedPath"] = os.path.abspath(outPath)
    setupContainer(r)
