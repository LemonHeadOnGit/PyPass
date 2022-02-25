"""
This file contains the password generation algorithm(s)
"""

from math import *
import random
import os
import time
from enum import Enum

class Password_Type(Enum):
    ONLY_NUMBERS = 1
    ONLY_LETTERS = 2
    NUMBES_AND_LETTERS = 3
    RANDOM_CHARS_AND_SYMBOLS = 4
    USER_SPECIFIED = 5

class PasswordGen():
    letterseta = "QqWwEeRrTtYyUuIiOoPp"
    lettersetb = "AaSsDdFfGgHhJjKkLl"
    lettersetc = "ZzXxCcVvBbNnMm"
    numseta = "1234567890"
    numsetb = "0987654321"

    letterset = [letterseta,lettersetb,lettersetc]
    numset = [numseta,numsetb]
    charset = [letterset,numset]
    secrand = random.SystemRandom()
    pword = ""
    pwordchars = ""
    pwordhash = ""

    def __init__(self):

        self.b = 0
        self.current_randomization = 0

        self.clear_screen()
        user_choice = -1

        while not self.is_valid_choice(user_choice):
            user_choice = self.get_users_choice()
        self.user_choice = Password_Type(user_choice)

    
    def clear_screen(self):
        if os.name == 'nt':
            opsys = 'cls'
        else: opsys = 'clear'

        os.system(opsys)
    
    def get_users_choice(self):
        self.charcount = int(input("How many characters do you want?\n\nChoice: "))
        self.clear_screen()
        passtype = int(input("Type of password?\n[1] Numbers\n[2] Letters\n[3] Numbers and Letters\n[4] Random characters (incl. symbols)\n[5] User specified list\n\nChoice: "))
        self.clear_screen()
        self.total_randomizations = int(input("How many times do you want the password to be randomized?\n(Nothing less than 1)\n\nChoice: "))
        print("Password will be randomized",self.total_randomizations,"times.")
        return passtype
    
    def is_valid_choice(self,choice):
        if choice in [1,2,3,4,5]:
            return True
        return False
    
    def get_password(self):
        print("Generating and randomizing...")
        if self.user_choice ==  Password_Type.ONLY_NUMBERS:
            while self.b < self.charcount:
                while self.current_randomization < self.total_randomizations:
                    numsetchoice = self.secrand.choice(self.numset)
                    i = random.randint(0,len(numsetchoice)-1)
                    self.pwordchars = self.pwordchars + numsetchoice[i]
                    self.current_randomization += 1
                i = random.randint(0,len(self.pwordchars)-1)
                pwordc = self.pwordchars[i]
                self.pword = self.pword + pwordc
                self.pword.replace(" ","")
                self.pwordchars = ""
                self.b = self.b + 1
                self.current_randomization = 0
        
        elif self.user_choice == Password_Type.ONLY_LETTERS:
            while self.b < self.charcount:
                while self.current_randomization < self.total_randomizations:
                    lettersetchoice = self.secrand.choice(self.letterset)
                    i = random.randint(0,len(lettersetchoice)-1)
                    self.pwordchars = self.pwordchars + lettersetchoice[i]
                    self.current_randomization += 1
                i = random.randint(0,len(self.pwordchars)-1)
                pwordc = self.pwordchars[i]
                self.pword = self.pword + pwordc
                self.pword.replace(" ","")
                self.pwordchars = ""
                self.b += 1
                self.current_randomization = 0

        elif self.user_choice == Password_Type.NUMBES_AND_LETTERS:
            timeremain = 0.00
            while self.b < self.charcount:
                starttime = time.time()
                while self.current_randomization < self.total_randomizations:
                    charsetchoice = self.secrand.choice(self.charset)
                    charcharsetchoice = self.secrand.choice(charsetchoice)
                    i = random.randint(0,len(charcharsetchoice)-1)
                    self.pwordchars = self.pwordchars + charcharsetchoice[i]
                    self.current_randomization += 1
                i = random.randint(0,len(self.pwordchars)-1)
                pwordc = self.pwordchars[i]
                self.pword = self.pword + pwordc
                self.pword.replace(" ","")
                self.pwordchars = ""
                self.b = self.b + 1
                self.current_randomization = 0
                endtime = time.time()
                timeremain = (endtime - starttime) * (self.charcount - self.b)

        elif self.user_choice == Password_Type.RANDOM_CHARS_AND_SYMBOLS:
            symseta = input("Specify the sets of symbols you want in set A: ")
            symsetb = input("Specify the sets of symbols you want in set B: ")
            symset = [symseta,symsetb]
            symsetc = [self.letterset,self.numset,symset]
            while self.b < self.charcount:
                while self.current_randomization < self.total_randomizations:
                    symsetchoice = self.secrand.choice(symsetc)
                    symsymsetchoice = self.secrand.choice(symsetchoice)
                    i = random.randint(0,len(symsymsetchoice)-1)
                    self.pwordchars = self.pwordchars + symsymsetchoice[i]
                    self.current_randomization += 1
                    self.clear_screen()
                    print("-----CHARACTER SET-----\n",self.pwordchars,"\n-----------------------\nGenerating password:",self.pword,"\n\nSTATS\n-----\nCurrent letter being generated:",str(self.b+1),"out of",self.charcount,"\nGenerated characters for letter:",str(self.current_randomization))
                i = random.randint(0,len(self.pwordchars)-1)
                pwordc = self.pwordchars[i]
                self.pword = self.pword + pwordc
                self.pword.replace(" ","")
                self.pwordchars = ""
                self.b = self.b + 1
                self.current_randomization = 0
        
        print("Hashing...")
        time.sleep(1)
        
        for i in self.pword:
            chn = ord(i) + 73
            self.pwordhash += chr(chn)
            print(i + " => " + self.pwordhash)
            time.sleep(.01)
        
        self.clear_screen()
        print("Your generated password is:",self.pwordhash)
        
        time.sleep(2)
        self.clear_screen()
        return self.pwordhash
