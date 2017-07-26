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

def getWorkspaceId():
    f = open(config.LOCALCONFIG, 'r')
    wid = f.read()
    f.close()
    return wid

def setWorkspaceId(wid):
    f = open(config.LOCALCONFIG, 'w')
    f.write(wid)
    f.close()

def getWorkingBranch():
    r = Repo(".")
    return r.active_branch.name
