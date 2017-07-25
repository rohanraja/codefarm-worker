import unittest
import time
from containers import *
from filetransfers import *

testRequest = {
        "sessionId": "testid1",
        "workspaceId": "wid1",
        "branchName": "aio",
        "repoUrl": "https://github.com/rohanraja/dotfiles",
        "image": "5aaddb01",
        "imageUrl": "http://localhost:8000/5aaddb011231.tar",
        "cmd": "make serve",
        "publishPorts": True,
        "ports": [3000],
        "srcPath": "/app2",
        "localClonedPath": "/Volumes/Fireice/Users/rraja/code/mshack17/railsapp/",
}

class ContainersTest(unittest.TestCase):

    def test_setupContainer(self):
        # hostImageFile()
        # time.sleep(6)
        setupContainer(testRequest)
        # time.sleep(3)
        print getExposedPorts(testRequest)

