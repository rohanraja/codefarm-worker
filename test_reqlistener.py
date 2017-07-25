import unittest
from requestListener import *

queueName = "testQueue1"
workerId = "1"

testMsg = """{
"type": "build",
"payload": {
"sessionId": "testid1",
"branchName": "master",
"repoUrl": "https://github.com/rohanraja/samplerails",
"image": "5aaddb01",
"imageUrl": "http://192.168.0.103:8000/5aaddb011231.tar",
"cmd": "make serve",
"publishPorts": "True",
"srcPath": "/app2"
}
}"""

class ReqListenerTest(unittest.TestCase):

    def Test_message_loop(self):
        requestLoop(workerId)

    def Test_message_loop_async(self):
        runRequestLooper(workerId)

    def Test_processing_request(self):
        processMessage(testMsg)
