import time as t

import paramiko

p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # This script doesn't work for me unless this line is added!
p.connect("169.63.183.157", port=22, username="root", password="")
stdin, stdout, stderr = p.exec_command("hostname")
t.sleep(5)
opt = stdout.readlines()
opt = "".join(opt)
print(opt)