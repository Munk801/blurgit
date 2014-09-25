
# Imports
import getpass
import os
from pygit2 import Repository, clone_repository
import re
import sys

class Repo(object):
	def __init__(self, path="", branch="develop"):
		self.path = path if path else os.getcwd()
		try:
			self.repo = Repository(self.path)
		except KeyError:
			self.repo = None
		# TODO Handle this another way
		self.repourl = "http://192.168.12.125/stephenl/blurrd.git"
		self.branch = branch

	def clone(self):
		self.repo = clone_repository(
			self.repourl,
			self.path,
			checkout_branch=self.branch
		)

	def createBranch(self, name):
		# TODO check if a branch of this name exists
		self.currentBranch = self.repo.create_branch(name, self.repo.head.get_object())
		self.repo.checkout(branch)

	def merge(self, branch, delete=False, push=False):
		currentRef = self.repo.head
		developBranch = self.repo.lookup_branch(branch)
		self.repo.checkout(developBranch)
		self.repo.merge(self.currentBranch.target)
		if delete:
			self.currentBranch.delete()
		if push:
			remote = self.repo.create_remote('origin', self.repo.path)
			remote.push(self.repo.head.name)

	def release(self):
		pass
