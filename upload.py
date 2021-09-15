import os
import time

"Auto uplaod for linux"

filename = "/home/paul/Schreibtisch/github token"

with open(filename, "r") as f:

    token = f.read()


#starting operation
os.system("git pull")
os.system("git add .")
os.system("git commit -m autosave")
os.system("git push")
