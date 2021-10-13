"""
Tokenizer parses the datalist given into tokens to give to Lexer that will compile the tokens to actual
python code
"""

import re
from Compiler.exceptions import (ConfigInstructionNotFound)

class Tokenizer:

    """
    Takes a dict and parses it into tokens
    """

    ConfigTokens = [

    ".title",
    ".fps",

    ]

    CodeTokens = {

    }

    def __init__(self, data):

        self.data = data

        #creating search strings
        self.config_search_strings = [r"\s*("+el+r")\s*([a-zA-Z0-9_]+)\s*$" for el in Tokenizer.ConfigTokens]

    def parse(self):

        """
        gives back a dictionary with parsed lines
        """

        back = {}

        #analyzing .config and <.CONFIG> line
        for el in self.data:
            #for key in self.data
            if el == ".config" or el == "<.CONFIG>":

                #starting dissection
                for value in self.data[el]:

                    #getting a list with all instructions
                    if not value:
                        continue

                    found = ""
                    current_config_token = ""

                    for search_string in self.config_search_strings:

                        found = re.search(search_string, value)
                        if found:
                            break

                    if not found:

                        raise ConfigInstructionNotFound()

                    back[found.groups()[0]] = found.groups()[1]





        return back
