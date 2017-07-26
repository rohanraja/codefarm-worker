import socket
import config
import json
from git import Repo

def getLocalIP():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = (s.getsockname()[0])
    s.close()
    return ip


def getProjInfo():
    f = open(config.FARMFILE, 'r')
    conts = f.read()
    f.close()
    fdict = json.loads(conts)
    return fdict

def getLocalConfig():
    try:
        f = open(config.LOCALCONFIG, 'r')
        conts = f.read()
        f.close()
        confg = json.loads(conts)
        return confg
    except:
        return {}

def saveConfig(c):
    strData = json.dumps(c)
    f = open(config.LOCALCONFIG, 'w')
    f.write(strData)
    f.close()

def getWorkspaceId():
    return getLocalConfig()["workspaceId"]

def getActiveSession():
    return getLocalConfig()["activeSession"]

def setActiveSession(sid):
    c = getLocalConfig()
    c["activeSession"] = sid
    saveConfig(c)

def setWorkspaceId(wid):
    c = getLocalConfig()
    c["workspaceId"] = wid
    saveConfig(c)

def getWorkingBranch():
    r = Repo(".")
    return r.active_branch.name
