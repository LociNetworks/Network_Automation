#!/usr/bin/env python
##############
# Author: Malachi
#
#
#
#
###############

import paramiko
import getpass

#Set variables and 
ssh = paramiko.SSHClient()
host = raw_input("What is the host name?: ")
user = raw_input("What is your username?: ")

#Set password variable while validating password entered was correctly entered
while True:
	passwd1 = getpass.getpass("What is your password?: ")
	passwd2 = getpass.getpass("Verify Password: ")
	if passwd1 != passwd2:
		print "Passwords do not match, please re-enter your password"
		continue
	else:
		passwd = passwd1
		break

#Automagically add ssh keys to known hosts
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

#Connect to host specified 
ssh.connect(host, username=user, password=passwd)

#submit command
stdin, stdout, stderr = ssh.exec_command("show bgp summary")
#Print output of command to console
output = stdout.read()
print "#####################################"
print "##### Requested Output is below #####"
print "#####################################"
print output



