import os
import time
import keyboard
import threading

"""Auto upload for linux"""

filename = "/home/paul/Schreibtisch/github token"
username = "pycppdel"

with open(filename, "r") as f:

    token = f.read()

class OP(threading.Thread):
    ended = False

    def run(self):
        os.system("git pull")
        os.system("git add .")
        os.system("git commit -m autosave")
        os.system("git push")
        OP.ended = True

class KB(threading.Thread):

    def run(self):
        while not OP.ended:
            pass
        print(token)




op = OP()
kb = KB()

op.start()
kb.start()

op.join()
kb.join()
