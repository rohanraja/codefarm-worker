import unittest
from containers import *

testRequest = {
        "sessionId": "testid1",
        "workspaceId": "wid1",
        "branchName": "aio",
        "repoUrl": "https://github.com/rohanraja/dotfiles",
        "image": "railwithdeps",
        "cmd": "make serve",
        "publishPorts": True,
        "srcPath": "/app2",
        "localClonedPath": "/Volumes/Fireice/Users/rraja/code/mshack17/railsapp/",
}

class ContainersTest(unittest.TestCase):

    def test_setupContainer(self):
        setupContainer(testRequest)

