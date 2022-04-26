#!/usr/bin/python3

import os
import subprocess

cwd=os.getcwd()
repo_name="python-git-demo"
repo_url="https://github.com/sahilsuri008/"+repo_name
path=cwd+repo_name

isFile = os.path.isfile(path) 

if isFile:
	print (path)
else:
	subprocess.call(["git", "clone", repo_url ])
