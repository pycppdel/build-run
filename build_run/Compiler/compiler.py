"""
Class Compiler compiles the given Code into an Dictionary, that will be given to
Pythonizer Class.
"""
#importing os and sys
import os
import sys
#getting exceptions
from exceptions import (PathNotFoundError, IsNoPlainFile,\
SectionsNotProperlySet)

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

        #checking for valid naming aka .plain
        if not self.filepath.endswith(".plain"):
            #does not end
            raise IsNoPlainFile(self.filepath)

        #path does exist and is .plain -> going on
        #opening file and reading data
        self.file = open(self.filepath, "r")

        #saving read
        self.filecode = self.file.read()
        #seeking back
        self.file.seek(0)
        #getting lines
        self.filecode_lines = [el.strip() for el in self.file.readlines()]
        #seeking back
        self.file.seek(0)

        #checking if the sections are loaded and located in the right way
        if not self.sectioncheck():
            #Sections are not properly set
            raise SectionsNotProperlySet(self.filepath)

        #finally: closing file
        self.file.close()

    def sectioncheck(self):
        """
        checks for the right section format inside the file.

        Section Order:

        1: .include //optional
        2: .config
        3: .data //optional
        4: .code
        """

        #generating regex patterns for checking existance and right order

        include_pattern = r"\s*\.include\s*$"
        config_pattern = r"\s*\.config\s*$"
        data_pattern = r"\s*\.data\s*$"
        code_pattern = r"\s*\.code\s*$"

        #line counter for the found line
        self.include_line = None
        self.config_line = None
        self.data_line = None
        self.code_line = None

        #counter for lines
        linecounter = 0


        #starting finding process
        #iterating over all lines
        for el in self.filecode_lines:

            #checking everything
            if self.include_line is None:

                if re.search(include_pattern, el):

                    #found
                    self.include_line = linecounter



            if self.config_line is None:

                if re.search(config_pattern, el):

                    #found
                    self.config_line = linecounter

            if self.data_line is None:

                if re.search(data_pattern, el):

                    #found
                    self.data_line = linecounter


            if self.code_line is None:

                if re.search(code_pattern, el):

                    #found
                    self.code_line = linecounter



            linecounter += 1

        #all lines have beend located

        #starting validation


        missing_section = (self.config_line is None or self.code_line is None)

        if missing_section:
            #section is missing
            return False

        #checks if the sections are in invalid order
        invalid_order = (self.code_line < self.config_line)

        #adding if data was detected
        if self.data_line is not None:
            invalid_order = (invalid_order or self.data_line < self.config_line)

        if self.include_line is not None:
            invalid_order = (invalid_order or self.code_line < self.include_line\
                             or self.config_line < self.include_line)

        if self.data_line is not None and self.include_line is not None:
            invalid_order = (invalid_order or self.data_line < self.include_line)

        if invalid_order:
            return False

        return True


        """
        TODO: checking validation for files that were included
        """





Compiler(sys.argv[1]).compile()
