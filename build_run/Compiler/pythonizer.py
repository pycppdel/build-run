"""
File with a class that generates python code from given Dictionary of Data.

Loads Libraries automatically
"""
import sys
import os
import platform
from Compiler.system_ import SYSTEM


SYSTEM.setSYSTEM()
syscalls = SYSTEM.getSYSTEMcalls()

class Pythonizer:

    """
    main class for generating a .py file
    """

    def __init__(self, code, pyname, exename=""):

        """
        gets the code as a dictionary of the different instructions
        """

        self.code = code
        self.pyname = pyname.split(".plain")[0]
        self.pyname += ".py"
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

            """
            for all instructions before loop from code
            """

            for el in self.code["beforeLoop"]:

                print(el)

            print('def redraw():')
            print('    screen.fill((255, 255, 255))')
            """
            for all instructions between draw from code
            """

            for el in self.code["insideDraw"]:

                print("    "+el)
            print('    pygame.display.flip()')
            print()
            print('while not ende:')
            print()
            print('    clock.tick(fps)')
            print()
            print('    for event in pygame.event.get():')
            print('        if event.type == pygame.QUIT:')
            print('            ende = True')
            """
            for all instructions inside loop loop from code
            """

            for el in self.code["insideLoop"]:

                print("    "+el)
            print()
            print('    redraw()')
            print()
            """
            for all instructions aftere loop from code
            """

            for el in self.code["afterLoop"]:

                print(el)
            print('pygame.quit()')


            sys.stdout = sys.__stdout__

        return True

    def compile_to_exe(self):
        """
        needs to be called after compiling to an py file
        """
        #quicksaving
        current_path = os.getcwd()
        #getting directory
        dirname = os.path.dirname(self.pyname)
        if dirname:
            os.chdir(dirname)
        #making exe

        try:

            os.system("pyinstaller --onefile "+os.path.basename(self.pyname))
            os.chdir("dist")
            os.system(syscalls["copy"]+" "+os.path.basename(self.pyname.split(".py")[0])+" .."+syscalls["divsign"])
        except:

            os.chdir(current_path)

            return False

        os.chdir(current_path)

        return True
