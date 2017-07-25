import unittest
from gitapi import *

testRepo = "https://github.com/rohanraja/samplerails"
branchName = "master"
repoPath = "./tmp/testRepo"

class GitTest(unittest.TestCase):

    def test_cloning_githubrepo(self):
        cloneBranch(testRepo, branchName, repoPath)

    def Test_pulling_branch(self):
        pullBranch(repoPath)
