import unittest
from filetransfers import *
import time

testRepo = "https://github.com/rohanraja/dotfiles"
branchName = "aio"
repoPath = "./tmp/testRepo"

class FileTransfersTest(unittest.TestCase):

    def test_requesting_imagefile(self):
        # hostImageFile()
        # time.sleep(6)
        imname = "http://192.167.1.51:8000/tst1.tar"
        path = requestImageFromServer(imname, "1815")

    def Test_hosting_imagefile(self):
        hostImageFile()

    def Test_listingImages(self):
        print getLocalImagesList()
