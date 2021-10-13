"""
Lexer transforms tokens from tokenizer into valid code for the pythonizer
"""

from Compiler.tokenizer import Tokenizer

class Lexer:



    """
    starts transforming process, returns a dictionary with all instructions: beforeLoop, insideDraw, insideLoop, afterLoop
    """

    def __init__(self, data):

        self.data = data

    def lex(self):

        """
        starts lexing all together
        """

        back = {"beforeLoop": [],
                "insideDraw": [],
                "insideLoop": [],
                "afterLoop": [],
                }

        for el in self.data:

            """
            disection starts
            """

            if el in Tokenizer.ConfigTokens:

                if el == ".title":

                    #title found. Instruction for setting title
                    back["beforeLoop"].append("pygame.display.set_caption('"+self.data[el]+"')")


        return back
