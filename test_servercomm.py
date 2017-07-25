import unittest
from servercomm import *
from sessionsManager import *
import config

wid = "1"

class ServerCOMMTest(unittest.TestCase):

    def Test_requesting_server(self):
        getMessageResponse({})

    def test_status_dispatcher(self):
        blockingStatusDispatcher(wid)
