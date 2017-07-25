import unittest
from redisutils import *
from test_reqlistener import testMsg

queueName = "worker_1"

class RedisTest(unittest.TestCase):

    def test_queuing_item_in_queue(self):
        queueMessage(queueName, testMsg)
        # getMessage(queueName)

