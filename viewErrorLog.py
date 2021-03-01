#!/usr/bin/env python3

from pexpect import pxssh
import time
s = pxssh.pxssh()
ip = "" #replace ip address
username= "" #replace username
password= "" #replace password
s.login (ip, username, password)
print ("SSH session login successful")
s.sendline ('tail -500 /opt/logs/Application.log | grep \'ERROR\'')
s.prompt()         # match the prompt
print(s.before)
s.logout()
