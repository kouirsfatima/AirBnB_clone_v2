#!/usr/bin/env bash
from os.path import isdir 
from datetime import datetime
from fabric.api import local

def do_pack():
	"""
		Generate a .tgz archive from the contents of the web_static folder.
		"""

		file_name = "versions/web_static_{}.tgz".format(
				datetime.now().strftime("%Y%m%d%H%M%S")
				)
		if not isdir("versions"):
		if local("mkdir -p versions").failed is True:
		return None
		if local("tar -cvzf {} web_static".format(file_name)).failed is True:
		return None
		return file_name

