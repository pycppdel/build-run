"""
Main file that invokes the transformation Process from .plain to
.exe, .py or linux executable.


"""

#for argv checking
import sys


#loading all modules needed for compilation
from Compiler.compiler import Compiler
from Compiler.pythonizer import Pythonizer


filename = sys.argv[1]

print(Pythonizer({}, "h.py").compile_to_py())
