from redisutils import *

projects = RedisObj("projects")
workspaces = RedisObj("workspaces")
workerImages = RedisObj("workerImages")
sessions = RedisObj("sessions")
statuses = RedisObj("statuses")

def addProjectInfo(wid, proj):
    projects[wid] = proj

def initDev(ipaddr, projInfo):
    print "Initializing FARM environment"

    ws = workspaces.get(ipaddr, [])

    wid = len(ws) + 1
    ws.append(wid)

    addProjectInfo(wid, projInfo)

    workspaces[ipaddr] = ws
    return wid


def initWorker(ipaddr, images):
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
    print "Requesting FARM to build"

    projInfo = projects[wid]
    imageId = projInfo["image"]

    workerIp, found = selectWorkerMachine(imageId)

    imgUrl = ""
    if found:
        imgUrl = getImageUrl(workerIp, imageId)

    sid = createOrGetSession(workerIp)

    queueBuildRequest(sid, workerIp, projInfo, imgUrl)



