#!/usr/bin/python -OO

#
# remote.xml in the config folder defines a custom action to run this script on "red"  button
#

import os

lockfile = "/tmp/hyperion.stopped"


if os.path.exists(lockfile):
	os.unlink(lockfile)
	os.system("sudo service hyperion stop") 
else:
	open(lockfile, 'a').close()
	os.system("sudo service hyperion start")
	
