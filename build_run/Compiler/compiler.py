"""
Class Compiler compiles the given Code into an Dictionary, that will be given to
Pythonizer Class.
"""
#importing os and sys
import os
import sys
#import from higher files
from exceptions import (PathNotFoundError, IsNoPlainFile)

import re

class Compiler:

    """
    Main class for compiling the file
    """

    def __init__(self, filepath):
        #gets the filepath for the file to compile.
        #compiler only maps includes of other files onto the dictionary.
        #if any of the pathes couldn't be fined the pythonizer will deal with it.

        self.filepath = filepath


    def compile(self):

        """
        invokes compilation process.

        returns back the compiled dictionary with all the data needed
        """

        #first: if file does not exist Exception needs to be thrown

        if not os.path.exists(self.filepath):
            #filepath does not exist

            #ready to be caught by Pythonizer
            raise PathNotFoundError(self.filepath)

        #path does exist -> going on
        #opening file and reading data
        self.file = open(self.filepath, "r")
        #saving read

        #checking if the sections are loaded and located in the right way
        self.sectioncheck()

        #finally: closing file
        self.file.close()

    def sectioncheck(self):
        """
        checks for the right section format inside the file.

        Section Order:

        1: .include
        2: .config
        3: .data
        4: .code
        """
        pass

Compiler(sys.argv[1]).compile()
