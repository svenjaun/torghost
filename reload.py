import sys
import time
from requests import get
import subprocess


print("Important!!!!! Use the magic word 'sudo'!")
if len(sys.argv) <= 1:
    print("Write seconds as argument: python3 reload.py 60 # Every 60 seconds")
    sys.exit(-1)


res = subprocess.check_output(['python3', 'torghost.py', '-s'])
print("Started TorGhost")

ip = get('https://api.ipify.org').content.decode('utf8')

print('IP address starts with: {}'.format(ip))

print("arg:", sys.argv[1])
running = True
print("Starting reloader")
while(running):
    time.sleep(int(sys.argv[1]))
    res = str(subprocess.check_output(['python3', 'torghost.py', '-r']))
    print("Reloaded")

    newip = get('https://api.ipify.org').content.decode('utf8')
    print('IP address starts with: {}'.format(newip))
