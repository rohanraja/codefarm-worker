import unittest
from requestProcessor import *


testRequest = {
        "sessionId": "testid1",
        "workspaceId": "wid1",
        "branchName": "master",
        "repoUrl": "https://github.com/rohanraja/samplerails",
        "image": "5aaddb01",
        "imageUrl": "http://192.167.1.51:8000/5aaddb011231.tar",
        "cmd": "make serve",
        "publishPorts": True,
        "srcPath": "/app2",
}

class WorkerRequestsTest(unittest.TestCase):

    def test_build_request(self):
        processBuildRequest(testRequest)

