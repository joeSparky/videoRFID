#!/usr/bin/python3.5
import subprocess
class RfidEventPath:
 def get(self):
  result = subprocess.run('ls /dev/input/event*',shell=True, stdout = subprocess.PIPE)
  for thisInput in result.stdout.splitlines():
   thisInput = thisInput.decode("utf-8")
   command = "udevadm info -q symlink -n "+ thisInput
   udevResults = subprocess.run(command, shell=True, stdout = subprocess.PIPE)
   for udevStr in udevResults.stdout.splitlines():
    udevStr = udevStr.decode("utf-8")
    if "Sycreader" in udevStr:
     return str(thisInput)
  return "fileDoesNotExist"
