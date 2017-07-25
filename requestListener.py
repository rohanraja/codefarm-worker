from redisutils import *
import threading
import json
from requestProcessor import *

processorsDict = {
        "build": processBuildRequest
}


def getQueueName(workerId):
    return "worker_%s"%workerId

def requestLoop(workerId, messageProcessor=None):

    qName = getQueueName(workerId)

    while True:

        msg = getMessage(qName)
        print "GOT MESSAGE from redis : %s" % msg
        if messageProcessor != None:
            messageProcessor(msg)


def processMessage(msg):
    outp = json.loads(msg)
    methodd = processorsDict[outp["type"]]
    methodd(outp["payload"])




def runRequestLooper(workerId):

    threading.Thread(target=requestLoop, args=(workerId,)).start()
