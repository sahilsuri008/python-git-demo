#!/usr/bin/python3

import os
import subprocess

cwd=os.getcwd()
repo_name="python-git-demo"
repo_url="https://github.com/sahilsuri008/"+repo_name
path=cwd+"/"+repo_name

isFile = os.path.isdir(path) 

if isFile:
	print ("Pulling latest files from BitBucket")
	os.chdir(repo_name)
	subprocess.call(["git", "pull"])
	os.chdir(cwd)
else:
	print(path)
	print("Repo does not exist. Cloning.")
	subprocess.call(["git", "clone", repo_url ])
