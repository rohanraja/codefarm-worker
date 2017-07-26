from redisutils import *
import json
from requestListener import getQueueName

def queueBuildRequest(sid, wid, proj, imUrl):

    outDict = {}
    outDict["type"] = "build"
    payload = {}

    payload["sessionId"] = sid

    payload = dict(payload.items() + proj.items())

    if imUrl != "":
        payload["imageUrl"] = imUrl

    outDict["payload"] = payload
    msg = json.dumps(outDict)
    queueName = getQueueName(wid)

    queueMessage(queueName, msg)


