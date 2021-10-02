"""
Class Compiler compiles the given Code into an Dictionary, that will be given to
Pythonizer Class.
"""
#importing os and sys
import os
import sys
#getting exceptions
from Compiler.exceptions import (PathNotFoundError, IsNoPlainFile,\
SectionsNotProperlySet, IncludeCrash, InvalidHeader)

import re

class Compiler:

    """
    Main class for compiling the file
    """

    def __init__(self, filepath, searchpaths=[]):
        #gets the filepath for the file to compile.
        #compiler only maps includes of other files onto the dictionary.
        #if any of the pathes couldn't be fined the pythonizer will deal with it.

        self.filepath = filepath

        #the folder for search paths
        self.searchpaths = searchpaths

        """
        MOST IMPORTANT:

        rawdata: data for the passed text only

        example:

        {

        '.config' : [//MULTIPLE LINES],
        '.code'   : [//MULTIPLE LINES],
        '<.CODE>' : [included lines of code]

        }

        """
        self.rawdata = {}


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

        #need to create the rawdata from the info of lines
        self.create_rawdata_from_sectioncheck()

        if not self.include_other_files():
            #include crashed
            raise IncludeCrash()


        #including other files if declared in .include

        #finally: closing file
        self.file.close()

        return self.rawdata


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

        #all lines have bee located

        #saving lines

        self.include_section_line_length = (self.config_line-self.include_line-1 if self.include_line else None)

        #.config length
        if self.data_line:

            self.config_section_line_length = (self.data_line-self.config_line-1)
            self.data_section_line_length = (self.code_line-self.data_line-1)

        else:

            self.config_section_line_length = (self.code_line-self.config_line-1)
            self.data_section_line_length = None

        #code length
        self.code_section_line_length = (linecounter-self.code_line-1)

        #starting validation

        """
        what will be given back: -> bool requirements_met
        """
        requirements_met = True

        """
        NEEDED: .config and .code segment
        """

        missing_section = (self.config_line is None or self.code_line is None)


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


        """


        Immediately stopping if the order is incorrect




        """

        if invalid_order:
            return False



        """
        starting check process for other files
        """

        #no search paths specified
        search_paths_invalid = False

        requirements_met = (not missing_section)

        return requirements_met

    def create_rawdata_from_sectioncheck(self):

        """
        starts adding all segments of the code into the rawdata
        """

        if self.include_line is not None:
            self.rawdata[".include"] = self.filecode_lines[self.include_line+1: self.include_line+self.include_section_line_length+1]

        if self.data_line is not None:
            self.rawdata[".data"] = self.filecode_lines[self.data_line+1: self.data_line+self.data_section_line_length+1]

        self.rawdata[".config"] = self.filecode_lines[self.config_line+1: self.config_line+self.config_section_line_length+1]
        self.rawdata[".code"] = self.filecode_lines[self.code_line+1: self.code_line+self.code_section_line_length+1]


    def include_other_files(self):
        """
        searches for other included files and adds their code to the main structure
        """

        #checking if something even was to be included

        includelines = self.filecode_lines[self.include_line+1:self.include_line+self.include_section_line_length+1]

        #generating datastring for include to fish out the filenames
        include_regex = r'\s*<include>\s*\"?([a-zA-Z0-9\._-]+)\"?\s*'

        #saving the paths to include
        paths_to_include = []

        #starting search
        for line in includelines:
            #dropping empty lines
            if not line:
                #back to next line
                continue

            #getting the declared filename
            filename = re.search(include_regex, line).groups()[0]

            #checking for existance
            if os.path.exists(filename):

                #exists
                paths_to_include.append(filename)
                continue
            else:
                #checking individually

                external_found = False
                for el in self.searchpaths:


                    if os.path.exists(el+filename):
                        #exists
                        paths_to_include.append(el+filename)
                        external_found = True

                if not external_found:
                    raise FileNotFoundError("Wrong include!")

        """
        included paths are now ready to be juiced out for code
        """

        #checking for validty
        for el in paths_to_include:

            #assigning filetype
            filetype = self.include_file_header_validity_check(el)

            #copying into code

        return True


    def include_file_header_validity_check(self, name):
        """
        checks for the specified file if it contains the right import header and gives back type of file.

        types are: '<.CONFIG>', '<.DATA>', '<.CODE>'
        """

        #header regexes
        config_header_regex = r"\s*(<\.CONFIG>)\s*"
        data_header_regex = r"\s*(<\.DATA>)\s*"
        code_header_regex = r"\s*(<\.CODE>)\s*"

        checks = [

        config_header_regex,
        data_header_regex,
        code_header_regex,

        ]

        return_type = ""

        #boolean for line with header
        had_header = False

        #line where header was found
        header_line_number = 0

        #counter for line
        current_line = 0

        #code for the file
        plaintext = {}

        #taking peak until line
        with open(name, "r") as f:

            #checking for line
            for line in f.readlines():

                current_line += 1

                if not line:
                    continue

                else:
                    #line has content
                    for check in checks:

                        found = re.search(check, line)

                        if found:
                            #found
                            had_header = True
                            return_type = found.groups()[0]
                            header_line_number = current_line
                            break

                    #line had content that was not the header -> invalid
                    if not had_header:

                        raise InvalidHeader(name)

                break

            #seeking back for code
            f.seek(0)

            #resetting current line
            current_line = 0

            #initilizing the plaintext dict
            plaintext[return_type] = []


            #adding all lines of code
            for line in f.readlines():

                current_line += 1

                if current_line <= header_line_number:
                    #no data yet
                    continue
                else:

                    #adding to data
                    line = line.strip()
                    plaintext[return_type].append(line)

        #finally: adding code to rawdata
        self.rawdata[return_type] = plaintext[return_type]

        return return_type
