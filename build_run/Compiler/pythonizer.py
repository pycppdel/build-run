"""
File with a class that generates python code from given Dictionary of Data.

Loads Libraries automatically
"""
import sys
import os


class Pythonizer:

    """
    main class for generating a .py file
    """

    def __init__(self, code, pyname, exename=""):

        """
        gets the code as a dictionary of the different instructions
        """

        self.code = code
        self.pyname = pyname #file of the outgoing py file
        self.exename = exename

    def compile_to_py(self):
        """
        compiles to a py at file pyname
        """

        with open(self.pyname, "w") as f:
            sys.stdout = f

            print('"""')
            print('File from flatterner ---- version 1.0')
            print('"""')
            print()
            print('import pygame')

            """
            Here all library imports
            """

            print()
            print('screen = pygame.display.set_mode((800, 800))')
            print()
            print('pygame.display.set_caption("DEMO APP")')
            print('fps = 60')
            print('ende = False')
            print()
            print('clock = pygame.time.Clock()')
            print()
            print('def redraw():')
            print('    screen.fill((255, 255, 255))')
            print('    pygame.display.flip()')
            print()
            print('while not ende:')
            print()
            print('    clock.tick(fps)')
            print()
            print('    for event in pygame.event.get():')
            print('        if event.type == pygame.QUIT:')
            print('            ende = True')
            print()
            print('    redraw()')
            print()
            print('pygame.quit()')


            sys.stdout = sys.__stdout__

    def compile_to_exe(self):
        """
        needs to be called after compiling to an py file
        """
        #quicksaving
        current_path = os.getcwd()
        print(os.path.dirname(self.pyname))
