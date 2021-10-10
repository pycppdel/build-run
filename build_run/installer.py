"""

installs all dependencies from build and run

"""

import os
import sys


filepath = None
#if file is not close enough path to build&run folder is needed
if not (os.getcwd().endswith("build_run")):
    #trying to get string
    if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):

        raise FileNotFoundError("No path input")
    else:
        filepath = sys.argv[1]
else:

    filepath = os.getcwd()

os.system("pip3 install -r "+filepath+"/dependencies.txt")
