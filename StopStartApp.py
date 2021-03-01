#!/usr/bin/env python3

from pexpect import pxssh
import time
s = pxssh.pxssh()
ip = "" #replace ip address
username= "" #replace username
password= "" #replace password
s.login (ip, username, password)
print ("SSH session login successful")
s.sendline ('application stop')
s.prompt()         # match the prompt
print("Stopping the app")

print("\nStarting the app")    
s.sendline ('application start')
s.prompt() 
print ("\nLogout")
s.logout()
