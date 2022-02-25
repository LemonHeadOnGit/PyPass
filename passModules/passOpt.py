r"""
Options for PyPass.
"""

import os
from enum import Enum
from passModules.passGen import PasswordGen
from passModules.passReader import passwordStorage
import subprocess

class Choice(Enum):
    SAVE_PASSWORD = 1
    GENERATE_PASSWORD = 2

class Options():
    def drawMenu(self):
        inChoice = True

        if os.name == "nt":
            opsys = "cls"
        else: opsys = "clear"

        os.system(opsys)

        while inChoice == True:
            userin = input("ENTER YOUR CHOICE:\n[1] Open Password Manager\n[2] Generate Password\nChoice: ")
        
            try: 
                if int(userin) == 1:
                    print("Opening password file...")
                    inChoice = False
                    passwordStorage.readPass()

                elif int(userin) == 2:
                    print("Opening password generator...")
                    inChoice = False
                    return PasswordGen.get_password()
                
                else: print("Invalid Choice")
            
            except TypeError:
                print("Invalid Choice")
                continue