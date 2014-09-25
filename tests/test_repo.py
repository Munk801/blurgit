
import pytest
import sys
sys.path.insert(0, r"C:\\")
from blurgit import Repo

def create_repo():
	repo = Repo(r"C:\\gitterdone")
	repo.clone()

def create_branch():
	repo = Repo(r"C:\\gitterdone")
	repo.clone()
	repo.createBranch("test")
	repo.merge("develop", delete=True, push=True)
	import pdb; pdb.set_trace()


if __name__ == "__main__":
	create_branch()
