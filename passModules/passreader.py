r"""
Password storage module.
"""

import os
from pathlib import Path
from enum import Enum
import subprocess

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
    pFile = Path(homedir + "/.pypass/.psfl")
    pDir = Path(homedir + "/.pypass")

    def __init__(self) -> None:
        homedir = str(Path.home())
        pFile = Path(homedir + "/.pypass/.psfl")
        pDir = Path(homedir + "/.pypass")
        
        self.initPassFile(pFile, pDir)

    def initPassFile(self, passFile : Path, pypassDir : Path):
        if pypassDir.is_dir() == False:
            pypassDir.mkdir(parents=True, exist_ok=True)
        if passFile.is_file() == False:
            with passFile.open('x') as f:
                f.close()
                subprocess.check_call(["attrib","+h",str(passFile)])
                subprocess.check_call(["attrib","+h",str(pypassDir)])

    def readPass(self, passFile: str):
        pass

    def savePass(self, passFile: str):
        pass

    def encryptDecrypt(self, passFile: str):
        pass