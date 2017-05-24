# Poorman Ramsomware Decrypter 0.33

from Crypto.Cipher import AES
import sys, time

key = "iamthekingofzu"
salt =  1461165993
key+= str(salt)

IV = 16 * '\x00'
mode = AES.MODE_CBC
decryptor = AES.new(key, mode, IV=IV)

data = open("important_password.png").read()
plaintext = decryptor.decrypt(data)

length = 16 - (len(plaintext) % 16)
plaintext += chr(length)*length


f = open("important_password.dec2.png", 'wb')
f.write(plaintext)
f.close()



