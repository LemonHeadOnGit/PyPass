import random

secrand = random.SystemRandom()
seperator = "-"

class Crypto:
    def __init__(self, message):
        self.message = message

    def encrypt(self):
        """
        Math encrypt Rules:
            * 234567898324567
            - 44
        """

        message = self.message
        chars = []
        for i in range(len(str(message))):
            char = message[i]

            chars.append(ord(char))

        encrypted = ''

        for ordi in chars:
            encrypted = encrypted + str((ordi * 234567898324567) - 44) + secrand.choice(seperator)

        self.message = encrypted
        return encrypted

    def decrypt(self):
        """
        Remember to use this when you're going to use it.
        """
        
        seperator = "-"
        decrypted = ''

        message = self.message
        chunk = []
       

        posssss = message.find(seperator)

        while posssss != -1:
            lengthMan = int(len(message))
            posTwoMan = posssss
            posThreeMan = posssss + len(seperator)

            chunk.append(message[0:posTwoMan])
            message = message[posThreeMan:lengthMan]

            posssss = message.find(seperator)
        
        
        for cnk in chunk:
            decrypted = decrypted + chr(int((int(cnk) + 44) / 234567898324567))
        return decrypted

manUrinates = Crypto(input("Enter message to encrypt: "))

# Encrypted
encryptedD = manUrinates.encrypt()

print("Encrypted: \n\n" + encryptedD + "\n")

# Decrypted

decryptedD = manUrinates.decrypt()

print('Decrypted: ' + decryptedD)