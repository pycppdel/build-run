import os
import time
import keyboard
import threading
import pyautogui

"""Auto upload for linux"""

filename = "/home/paul/Schreibtisch/github token"
username = "pycppdel"

with open(filename, "r") as f:

    token = f.read()

pyautogui.write("HEHE")

class OP(threading.Thread):
    ended = False

    def run(self):
        os.system("git pull")
        os.system("git add .")
        os.system("git commit -m autosave")
        OP.ended = True
        os.system("git push")

class KB(threading.Thread):

    def run(self):
        while not OP.ended:
            pass
        time.sleep(10)
        pyautogui.write(username)
        keyboard.press_and_release("enter")
        time.sleep(5)
        pyautogui.write(token)
        keyboard.press_and_release("enter")




op = OP()
kb = KB()

op.start()
kb.start()

op.join()
kb.join()
