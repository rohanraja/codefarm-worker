import unittest
from redisutils import *

queueName = "worker_1"

class RedisTest(unittest.TestCase):

    def test_queuing_item_in_queue(self):
        queueMessage(queueName, "testmsg11")
        # getMessage(queueName)

