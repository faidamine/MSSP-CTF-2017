key = 125
cipher = [int(x) for x in "234 240 240 237 224 241 227 248 209 174 234 226 220 209 174 234 226 220 205 177 225 220 209 174 234 226 250".split(' ')]
plain = [x-key for x in cipher]
print ''.join(chr(x) for x in plain)
