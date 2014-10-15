"""
###############################################################################
blurgit - Framework for manipulating and managing blur git repositories
###############################################################################

Blurgit is a framework for wrapping git commands to properly handle the blur
workflow for checking out, committing, and pushing changes to the blur git
repositories.

Blurgit uses a combination of pygit2 and gitpython to run the commands.

"""
# Imports
import getpass
import git
import os
from pygit2 import Repository, clone_repository
import re
import subprocess
import sys

class Repo(object):
	def __init__(self, path="", branch="develop"):
		self.path = path if path else os.getcwd()
		# Retrieve the repo if its already defined
		try:
			self.repo = Repository(self.path)
			# This is a little hacky, but we need a git command interface to do
			# certain things
			self.pygitrepo = git.Repo(self.repo.path)
			self.git = self.pygitrepo.git
			self.currentBranch = self.repo.lookup_branch(self.repo.head.shorthand)
			self._user = self.repo.default_signature
		except KeyError:
			self.repo = None
			self.currentBranch = None
			self._user = None
		# TODO Handle this another way
		self.branch = branch

	@property
	def user(self):
		if not self._user and self.repo:
			self._user = self.repo.default_signature
		return self._user

	def clone(self, repourl):
		self.repo = clone_repository(
			repourl,
			self.path,
			checkout_branch=self.branch
		)

	def checkoutBranch(self, name):
		# TODO check if a branch of this name exists
 		developBranch = self.repo.lookup_branch("develop")
		self.repo.checkout(developBranch)
		self.currentBranch = self.repo.create_branch(
			name,
			self.repo.head.get_object()
		)
		self.repo.checkout(self.currentBranch)

	def merge(self, branch, delete=False, push=False):
		pass

	def release(self):
		# Checkout the release branch
		# Need some way to control versioning
		# Internal versioning
		pass
