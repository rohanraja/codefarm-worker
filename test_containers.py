import unittest
import time
from containers import *
from filetransfers import *

# "image": "5aaddb01",
# "imageUrl": "http://192.167.1.51:8000/5aaddb011231.tar",


testRequestOLD = {
        "sessionId": "testid1",
        "workspaceId": "wid1",
        "branchName": "aio",
        "repoUrl": "https://github.com/rohanraja/dotfiles",
        "image": "5aaddb01",
        "imageUrl": "http://192.167.1.51:8000/5aaddb011231.tar",
        "cmd": "make serve",
        "publishPorts": True,
        "srcPath": "/app2",
        "localClonedPath": "/Volumes/Fireice/Users/rraja/code/mshack17/railsapp/",
}

testRequest = {
        "sessionId": "testid1",
        "workspaceId": "wid1",
        "branchName": "aio",
        "repoUrl": "https://github.com/rohanraja/dotfiles",
        "image": "1815",
        "imageUrl": "http://192.167.1.51:8000/1815.tar",
        "cmd": "",
        "publishPorts": False,
        "srcPath": "",
        "localClonedPath": "",
}

class ContainersTest(unittest.TestCase):

    def test_setupContainer(self):
        # hostImageFile()
        # time.sleep(6)
        setupContainer(testRequest)

