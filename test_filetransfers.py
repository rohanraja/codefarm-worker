import unittest
from filetransfers import *
import time

testRepo = "https://github.com/rohanraja/dotfiles"
branchName = "aio"
repoPath = "./tmp/testRepo"

class FileTransfersTest(unittest.TestCase):

    def Test_requesting_imagefile(self):
        hostImageFile()
        time.sleep(6)
        imname = "http://localhost:8000/tst1.tar"
        path = requestImageFromServer(imname, "1815")

    def Test_hosting_imagefile(self):
        hostImageFile()

    def test_listingImages(self):
        print getLocalImagesList()
