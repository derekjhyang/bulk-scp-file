#!/usr/bin/env python

import sys
import paramiko
from paramiko import SSHClient
from paramiko import AutoAddPolicy as auto_add_policy
from scp import SCPClient # from jbardin/scp.py (https://github.com/jbardin/scp.py)

remote_host = dict()
remote_host.setdefault('username', sys.argv[2])
remote_host.setdefault('password', sys.argv[3])


## new SSH client which works with SSH2 protocol ##
client = SSHClient()
client.set_missing_host_key_policy(auto_add_policy())
for ip in open(sys.argv[1]):
   client.connect(ip, **remote_host)
   #(stdin, stdout, stderr) = client.exec_command("ls -al")
   #print stdout.read(), stderr.read()
   scp = SCPClient(client.get_transport())
   scp.put(sys.argv[4],sys.argv[5])

## clean up ##
client.close()
