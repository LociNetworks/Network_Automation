#!/usr/bin/env python
##############
# Author: Malachi
#
#
#
#
###############

import getpass
from fabric import tasks
from fabric.api import run, env
from fabric.network import disconnect_all


env.hosts = raw_input("What is the IP?: ")
env.user = raw_input("What is your username?: ")
env.password = getpass.getpass("What is your password?: ")


def task():
	output = run('show bgp summary')

print output
