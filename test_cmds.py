import unittest
from main_dev import *
from main_worker import *
import time
import os

class SystemFullTest(unittest.TestCase):

    def test_initiating_machines_and_building(self):
        os.system("./stopAll.sh")
        init()
        initRepo()
        build()
        runDaemon()
        for i in range(10):
            status()
            time.sleep(1)

