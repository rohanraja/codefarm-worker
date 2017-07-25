import json

def getMessageResponse(msg):
    resp = {}

    print "*********"
    print "Sending MSG: %s" % msg
    print "##########"
    return resp


def sendServerMsg(msgtype, workerid, payload):

    msg = {
        "type":msgtype,
        "workerId":workerid,
        "payload":payload,
    }

    strMsg = json.dumps(msg)

    return getMessageResponse(strMsg)

