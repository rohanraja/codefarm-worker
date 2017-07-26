import unittest
from redisutils import *
from initcmds import *


class RedisCMDSTest(unittest.TestCase):

    def Test_init_worker(self):

        initWorker("192.168.0.100", ["1815", "5aa"])

    def test_get_status(self):

        stat = getSessionStats("testid1")
        print stat


