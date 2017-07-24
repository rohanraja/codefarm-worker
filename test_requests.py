import unittest
from requestProcessor import *


testRequest = {
        "sessionId": "testid1",
        "workspaceId": "wid1",
        "branchName": "aio",
        "repoUrl": "https://github.com/rohanraja/dotfiles",
}

class WorkerRequestsTest(unittest.TestCase):

    def test_build_request(self):
        processBuildRequest(testRequest)

