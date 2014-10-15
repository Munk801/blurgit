
import pytest
import sys
sys.path.insert(0, r"C:\\")
from blurgit import Repo

REPOPATH = r"C:\\TestRepo"

def create_repo():
	repo = Repo(REPOPATH)
	repo.clone()

def create_branch():
	repo = Repo(REPOPATH)
	repo.checkoutBranch("test")
	import pdb; pdb.set_trace()

def test_merge():
	repo = Repo(REPOPATH)
	import pdb; pdb.set_trace()
	repo.merge("develop", delete=False, push=False)

if __name__ == "__main__":
	test_merge()
	# create_branch()
