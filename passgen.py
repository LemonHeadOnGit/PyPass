"""
This file contains the password generation algorithm(s)
"""

from math import *
import random
import os
import time

def passwordgen():
    # --- GET OS ---

    if os.name == 'nt':
        opsys = 'cls'
    else: opsys = 'clear'

    os.system(opsys)

    # --- USER CHOICE ---

    charcount = int(input("How many characters do you want?\n\nChoice: "))
    os.system(opsys)
    passtype = int(input("Type of password?\n[1] Numbers\n[2] Letters\n[3] Numbers and Letters\n[4] Random characters (incl. symbols)\n\nChoice: "))
    os.system(opsys)
    a = int(input("How many times do you want the password to be randomized?\n(Nothing less than 1)\n\nChoice: "))
    b = 0
    c = 0
    print("Password will be randomized",a,"times.")

    time.sleep(2)

    # --- START GENERATION ---

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

    if passtype == 1:
        while b < a:
            print("1")

    elif passtype == 2:
        while b < charcount:
            while c < a:
                lettersetchoice = secrand.choice(letterset)
                i = random.randint(0,len(lettersetchoice)-1)
                pwordc = lettersetchoice[i]
                c = c + 1
                os.system(opsys)
                print(pwordc,"\nGenerating password:",pword)
            pword = pword + pwordc
            pword.replace(" ","")
            os.system(opsys)
            b = b + 1
            c = 0

    elif passtype == 3:
        while b < charcount:
            while c < a:
                charsetchoice = secrand.choice(charset)
                charcharsetchoice = secrand.choice(charsetchoice)
                i = random.randint(0,len(charcharsetchoice)-1)
                pwordc = charcharsetchoice[i]
                c = c + 1
                os.system(opsys)
                print(pwordc,"\nGenerating password:",pword)
            pword = pword + pwordc
            pword.replace(" ","")
            os.system(opsys)
            b = b + 1
            c = 0

    print("Your generated password is:",pword)