"""
This file contains the password generation algorithm(s)
"""

from math import *
import random
import os
import time
from progress.bar import Bar

def passwordgen(displayPass,toFile):
    """
    This is the module for generating the password.
    --------
     - displayPass: Whether the password should be displayed
                         in real time or not. True for yes.
     - toFile:      Whether the password should be sent to
                         a text file or not. True for yes.
    """
    # --- GET OS ---

    if os.name == 'nt':
        opsys = 'cls'
    else: opsys = 'clear'

    os.system(opsys)

    # --- USER CHOICE ---

    charcount = int(input("How many characters do you want?\n\nChoice: "))
    os.system(opsys)
    passtype = int(input("Type of password?\n[1] Numbers\n[2] Letters\n[3] Numbers and Letters\n[4] Random characters (incl. symbols)\n[5] User specified list\n\nChoice: "))
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
    pwordchars = ""

    if passtype == 1:
        while b < charcount:
            while c < a:
                numsetchoice = secrand.choice(numset)
                i = random.randint(0,len(numsetchoice)-1)
                pwordchars = pwordchars + numsetchoice[i]
                c = c + 1
                os.system(opsys)
                print("-----CHARACTER SET-----\n",pwordchars,"\n-----------------------\nGenerating password:",pword,"\n\nSTATS\n-----\nCurrent letter being generated:",str(b+1),"out of",charcount,"\nCurrent character generation value:",str(c))
            i = random.randint(0,len(pwordchars)-1)
            pwordc = pwordchars[i]
            pword = pword + pwordc
            pword.replace(" ","")
            pwordchars = ""
            b = b + 1
            c = 0

    elif passtype == 2:
        while b < charcount:
            while c < a:
                lettersetchoice = secrand.choice(letterset)
                i = random.randint(0,len(lettersetchoice)-1)
                pwordchars = pwordchars + lettersetchoice[i]
                c = c + 1
                os.system(opsys)
                print("-----CHARACTER SET-----\n",pwordchars,"\n-----------------------\nGenerating password:",pword,"\n\nSTATS\n-----\nCurrent letter being generated:",str(b+1),"out of",charcount,"\nCurrent character generation value:",str(c))
            i = random.randint(0,len(pwordchars)-1)
            pwordc = pwordchars[i]
            pword = pword + pwordc
            pword.replace(" ","")
            pwordchars = ""
            b = b + 1
            c = 0

    elif passtype == 3:
        timeremain = 0.00
        while b < charcount:
            starttime = time.time()
            while c < a:
                charsetchoice = secrand.choice(charset)
                charcharsetchoice = secrand.choice(charsetchoice)
                i = random.randint(0,len(charcharsetchoice)-1)
                pwordchars = pwordchars + charcharsetchoice[i]
                os.system(opsys)
                c = c + 1
                print("-----CHARACTER SET-----\n",pwordchars,"\n-----------------------\nGenerating password:",pword,"\n\nSTATS\n-----\nCurrent letter being generated:",str(b+1),"out of",charcount,"\nCurrent character generation value:",str(c),"\nRemaining time: +-",str(float("%.2f"%timeremain)),"seconds.")
            i = random.randint(0,len(pwordchars)-1)
            pwordc = pwordchars[i]
            pword = pword + pwordc
            pword.replace(" ","")
            pwordchars = ""
            b = b + 1
            c = 0
            endtime = time.time()
            timeremain = (endtime - starttime) * (charcount - b)

    elif passtype == 4:
        symseta = input("Specify the sets of symbols you want in set A: ")
        symsetb = input("Specify the sets of symbols you want in set B: ")
        symset = [symseta,symsetb]
        symsetc = [letterset,numset,symset]
        while b < charcount:
            while c < a:
                symsetchoice = secrand.choice(symsetc)
                symsymsetchoice = secrand.choice(symsetchoice)
                i = random.randint(0,len(symsymsetchoice)-1)
                pwordchars = pwordchars + symsymsetchoice[i]
                c = c + 1
                os.system(opsys)
                print("-----CHARACTER SET-----\n",pwordchars,"\n-----------------------\nGenerating password:",pword,"\n\nSTATS\n-----\nCurrent letter being generated:",str(b+1),"out of",charcount,"\nGenerated characters for letter:",str(c))
            i = random.randint(0,len(pwordchars)-1)
            pwordc = pwordchars[i]
            pword = pword + pwordc
            pword.replace(" ","")
            pwordchars = ""
            b = b + 1
            c = 0

    os.system(opsys)
    print("Your generated password is:",pword)
    time.sleep(1)
    os.system(opsys)
    return pword