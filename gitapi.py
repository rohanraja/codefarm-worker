import git

def cloneBranch(repoUrl, branch, outPath):
    repo = git.Repo.clone_from(repoUrl, outPath, branch=branch)

def pullBranch(git_dir):
    g = git.cmd.Git(git_dir)
    g.pull()
