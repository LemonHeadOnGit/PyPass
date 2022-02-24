r"""
Password storage module.
"""

import os
from pathlib import Path
from enum import Enum

class readChoice(Enum):
    READ_PASSWORDS = 1
    SAVE_PASSWORDS = 2
    ENCRYPT_FILE = 3
    DECRYPT_FILE = 4

class passwordStorage():
    r"""
    The class for password storage/reading.
    """

    homedir = str(Path.home())
    pFile = homedir + "/.pypass/.psfl"
    pDir = homedir + "/.pypass"

    def __init__(self) -> None:
        self.initPassFile()

    def initPassFile(self, passFile: pFile, pypassDir: pDir):
        pass
        if Path.exists(passFile) == False:
            with open(passFile) as f:
                f.write()
                f.close()
                os.system("attrib +h" + passFile)
                os.system("attrib +h" + pypassDir)

    def readPass(self, passFile: str):
        pass

    def savePass(self, passFile: str):
        pass

    def encryptDecrypt(self, passFile: str):
        pass