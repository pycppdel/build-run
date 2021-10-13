"""
file for all exceptions.
"""

class PathNotFoundError(Exception):

    """
    class for invalid path parsed
    """

    def __init__(self, path):
        self.path = path

    def __str__(self):
        #returns the error message
        return ("The Path "+self.path+" was not found.")

class IsNoPlainFile(Exception):

    """
    Class used for raising an error if a non .plain file was to be compiled
    """

    def __init__(self, path):
        self.path = path

    def __str__(self):
        #returns the error message
        return ("The Path "+self.path+" is no plain file.")

class SectionsNotProperlySet(Exception):

    """
    Exceptions for invalid headers
    """
    def __init__(self, path):
        self.path = path

    def __str__(self):
        #returns the error message
        return ("The Path "+self.path+" contains a invalid Section structure.")

class IncludeCrash(Exception):

    """
    Exception for when the include crashed
    """
    def __str__(self):

        return "The include crashed"

class InvalidHeader(Exception):

    """
    exception for when an included file as a wrong header
    """

    def __init__(self,filename):
        self.filename = filename

    def __str__(self):
        return self.filename+" has an invalid header. Valid headers are: <.CONFIG>, <.DATA>, <.CODE>"

class ConfigInstructionNotFound(Exception):

    def __str__(self):

        return "The instruction you declared in .config was not valid"
