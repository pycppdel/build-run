"""
Main file that invokes the transformation Process from .plain to
.exe, .py or linux executable.


"""

#for argv checking
import sys


#loading all modules needed for compilation
from Compiler.compiler import Compiler
from Compiler.tokenizer import Tokenizer
from Compiler.lexer import Lexer
from Compiler.pythonizer import Pythonizer


filename = sys.argv[1]
if not filename:

    raise FileNotFoundError("no input")

p = Pythonizer({}, sys.argv[1])
p.compile_to_py()
p.compile_to_exe()
