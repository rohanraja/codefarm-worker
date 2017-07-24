from gitapi import *
import os
import config

def getCloneDir(r):

    outp = os.path.join(config.WORK_DIR, r["sessionId"])
    return outp


def processBuildRequest(r):

    outPath = getCloneDir(r)
    cloneBranch(r["repoUrl"], r["branchName"], outPath)
    r["localClonedPath"] = outPath
    setupContainer(r)