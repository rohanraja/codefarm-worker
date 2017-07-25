from gitapi import *
import os
import config
from containers import *

def getCloneDir(r):

    outp = os.path.join(config.WORK_DIR, r["sessionId"])
    return outp


def processBuildRequest(r):

    print "Processing Build Request %s" % r

    outPath = getCloneDir(r)
    if(os.path.exists(outPath)):
        pullBranch(outPath)
    else:
        cloneBranch(r["repoUrl"], r["branchName"], outPath)
    r["localClonedPath"] = os.path.abspath(outPath)
    setupContainer(r)
