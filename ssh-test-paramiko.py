#!/usr/bin/env python
##############
# Author: Malachi
###############

import paramiko
import getpass

#Set variables and 
ssh = paramiko.SSHClient()
host = raw_input("What is the host name?: ")
user = raw_input("What is your username?: ")

#Set password variable while validating password entered was correctly entered
def passwd_check():
	while True:
		passwd1 = getpass.getpass('Enter your password: ')
		passwd2 = getpass.getpass('Re-enter your password to verify: ')
		if passwd1 != passwd2:
			print "Passwords do not match, please re-enter your password"
			continue
		elif passwd1 == passwd2:
			print "Password Accpeted"
			return passwd2


passwd = passwd_check()

# print passwd

#Automagically add ssh keys to known hosts
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

#Connect to host specified 
ssh.connect(host, username=user, password=passwd)

#submit command
stdin, stdout, stderr = ssh.exec_command(raw_input("Type a command: "))
#Print output of command to console
output = stdout.read()
print "#####################################"
print "#####  Requested Output Below   #####"
print "#####################################"
print output


