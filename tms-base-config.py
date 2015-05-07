#!/usr/bin/env python
from IPy import IP

#Get TMS hostname
print
tms_hostname = raw_input("What will the hostname for the TMS be? ")
print tms_hostname
print
#Get TMS IP and ensure it is a valid IP otherwise loop
while True:
	try:
		tms_ip = IP(raw_input("What will be the management IP for the TMS be? "))
		print tms_ip
		print
		break
	except ValueError:
		print("Please enter IP address in correct format")
		print("Example: 192.168.0.1")
		continue
	else:
		break
#Get MGT IP subnet mask and ensure that it is in a valid format
while True:
	try:
		tms_subnet = IP(raw_input("What is the subnet mask of the MGT IP? "))
		print tms_subnet
		print
		break
	except ValueError:
		print("Please enter subnet mask in correct format")
		print("Example: 255.255.255.0")
		continue
	else:
		break
#Get IP default Gateway and ensure it is in a valid format
while True:
	try:
		tms_gateway = IP(raw_input("What is the default gateway for the MGT IP? "))
		print tms_gateway
		print
		break
	except ValueError:
		print("Please enter default gateway in correct format")
		print("Example: 192.168.0.1")
		continue
	else:
		break
# Get Leader IP and ensure it is in a valid format
while True:
	try:
		tms_leader = IP(raw_input("What is the IP of the leader appliance? "))
		print tms_leader
		print
		break
	except ValueError:
		print("Please enter Leader IP in correct format")
		print("Example: 192.168.0.1")
		continue
	else:
		break

#Get Zone Secret
zone_secret = raw_input("What will the zone_secret be?: ")

# Anything below this line will print to console
print "################################################################################"
print "#####       Copy & Paste below configuration into TMS console              #####"
print "################################################################################"
print

#Set admin password
print "services aaa local password admin encrypted <admin encrypted password"

# Set system hostname
print "system name set %s" % tms_hostname

# Set up access ACL, then commit
print "ip access add ping all 192.168.0.0/24"
print "ip access add snmp all 192.168.0.0/24"
print "ip access add ssh all 192.168.0.0/24"
print "ip access commit"

# Setup managment interface for IP connectivity
print ("ip interface ifconfig mgt0 %s %s up" % (tms_ip, tms_subnet));

# Set default route for managment
print "ip route add default %s" % tms_gateway

# Start ssh services
print "services ssh start"

# Enabled access to shell
print "system attributes set shell.enabled = 1"

# Set leader appliance
print ("services tms bootstrap %s %s" % (tms_leader, zone_secret));

# Save all changes, changes will revert if not saved when rebooted
print "config write"
print
print "##### END #####"
print
