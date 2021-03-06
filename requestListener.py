from redisutils import *
import threading
import json
from requestProcessor import *

processorsDict = {
        "build": processBuildRequest,
        # "stopBuild" : processStopRequest
}

def getQueueName(workerId):
    return "worker_%s"%workerId

def processMessage(msg):
    outp = json.loads(msg)
    methodd = processorsDict[outp["type"]]
    methodd(outp["payload"])

def requestLoop(workerId):

    print "Starting request listener loop"
    qName = getQueueName(workerId)

    while True:
        msg = getMessage(qName)
        print "GOT MESSAGE from redis : %s" % msg
        processMessage(msg)


def runRequestLooper(workerId):
    threading.Thread(target=requestLoop, args=(workerId,)).start()
