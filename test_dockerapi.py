import unittest
from dockerapi import *


class DockerApiTest(unittest.TestCase):

    def Test_running_docker_CMD(self):
        dockerRun({
            "image": "railwithdeps",
            "cmd": "make serve",
            "publishPorts": True,
            "fromPath": "/Volumes/Fireice/Users/rraja/code/mshack17/railsapp/",
            "toPath": "/app2",
        })

    def Test_check_image_exits(self):

        assert imageExists("railwithdeps") == True
        assert imageExists("railwithdepsDUMMY") == False

    def Test_saving_image(self):

        saveImageToFile("railwithdeps", "tmp/railswithdeps.tar")

    def Test_loading_image(self):

        forceRemoteImg("1815")
        loadImageFromFile("tmp/images/1815.tar")
        assert imageExists("1815") == True

    def test_winpathConversion(self):

        assert converToWinDockPath("C:\\src\\test") == "//C/src/test"

# docker run -itP -v $(pwd):/app2 railwithdeps make serve
