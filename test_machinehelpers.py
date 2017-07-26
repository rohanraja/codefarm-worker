import unittest
from machineHelpers import *


class MachineHelpTest(unittest.TestCase):

    def test_getting_ip(self):
        print getLocalIP()

    def Test_loading_FARMFILE(self):
        print getProjInfo()

    def test_get_branch(self):
        print getWorkingBranch()
