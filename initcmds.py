from redisutils import *
from requestQueuer import *

projects = RedisObj("projects")
workspaces = RedisObj("workspaces")
workerImages = RedisObj("workerImages")
sessions = RedisObj("sessions")
statuses = RedisObj("statuses")

def addProjectInfo(wid, proj):
    projects[wid] = proj

def initDev(ipaddr, projInfo):
    print "Initializing FARM DEV environment"

    ws = workspaces.get(ipaddr, [])

    wid = len(ws) + 1
    ws.append(wid)
    workspaces[ipaddr] = ws

    addProjectInfo(wid, projInfo)

    return wid


def initWorker(ipaddr, images):
    print "Initializing FARM worker"
    updateWorkerImages(ipaddr, images)

def updateWorkerImages(ipaddr, images):
    workerImages[ipaddr] = images


def selectWorkerMachine(imageId):

    for workerIp in workerImages.keys():
        if imageId in workerIp:
            return workerIp, True

    return workerImages.keys()[0] , False

def getImageUrl(ip, imid):
    return "http://%s:%d/%s.tar" % (ip, 8000, imid)


def getSessionStats(sid):
    return statuses[sid]

def createOrGetSession(wid, newSess = False):
    sess = sessions.get(wid, [])

    if len(sess) > 0 and newSess == False:
        return sess[-1]
    
    sid = len(sess) + 1
    sess.append(sid)
    sessions[wid] = sess
    
    return sid


def requestBuild(wid, branch):
    print "Requesting FARM to build branch: %s" % branch

    projInfo = projects[wid]
    projInfo["branch"] = branch
    imageId = projInfo["image"]

    workerIp, found = selectWorkerMachine(imageId)

    imgUrl = ""
    if found:
        imgUrl = getImageUrl(workerIp, imageId)

    sid = createOrGetSession(workerIp)

    statuses[sid] = ["Requesting a worker to build"]

    queueBuildRequest(sid, workerIp, projInfo, imgUrl)



