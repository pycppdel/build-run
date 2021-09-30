"""
Class Compiler compiles the given Code into an Dictionary, that will be given to
Pythonizer Class.
"""

#imports
from build_run.exceptions import (PathNotFoundError)

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

        pass
