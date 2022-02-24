r"""
Options for PyPass.
"""

from enum import Enum


class Choice(Enum):
    SAVE_PASSWORD = 1
    GENERATE_PASSWORD = 2

class options():
    def drawMenu(self):
        print("ENTER YOUR CHOICE:\n[1] Open Password Manager\n[2] Generate Password\nChoice: ")