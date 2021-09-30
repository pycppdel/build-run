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
