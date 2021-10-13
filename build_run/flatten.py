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
from Compiler.exceptions import *


filename = sys.argv[1]
if not filename:

    raise FileNotFoundError("no input")

try:

    data = Compiler(sys.argv[1]).compile()


    parsed_data = Tokenizer(data).parse()

    lexed_data = Lexer(parsed_data).lex()

    print(lexed_data)


    p = Pythonizer(lexed_data, sys.argv[1])
    p.compile_to_py()
    p.compile_to_exe()

except PathNotFoundError:
    print("The given path to the .plain file was not found")
