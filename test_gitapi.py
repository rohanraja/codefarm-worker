import unittest
from gitapi import *

testRepo = "https://github.com/rohanraja/dotfiles"
branchName = "aio"
repoPath = "./tmp/testRepo"

class GitTest(unittest.TestCase):

    def Test_cloning_githubrepo(self):
        cloneBranch(testRepo, branchName, repoPath)

    def test_pulling_branch(self):
        pullBranch(repoPath)
