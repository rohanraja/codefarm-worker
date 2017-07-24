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

    def test_loading_image(self):

        loadImageFromFile("tmp/tst1.tar")
        assert imageExists("1815") == True


# docker run -itP -v $(pwd):/app2 railwithdeps make serve
