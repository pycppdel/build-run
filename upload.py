import os
import time
import keyboard

"""Auto upload for linux"""

filename = "/home/paul/Schreibtisch/github token"
username = "pycppdel"

with open(filename, "r") as f:

    token = f.read()


#starting operation
os.system("git pull")
os.system("git add .")
os.system("git commit -m autosave")
os.system("git push")
time.sleep(1)
print(token)
keyboard.write(username)
keyboard.press("enter")
time.sleep(1)
keyboard.write(token)
keyboard.press("enter")
