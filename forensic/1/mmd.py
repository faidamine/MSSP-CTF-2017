import hashlib
import string



alpha = string.printable
l = []
for letter in alpha:
    encrypt = hashlib.new("md5",string=letter)
    h = encrypt.hexdigest()
    f = open("hashes.txt").read()
    lines = f.split('\n')
    for x in lines:
        if x == h:
            l.append(letter)
            print letter

print "".join(l)
print "Finished"

