#!/usr/bin/env python3

import binascii
import base64
import itertools

key = 'mokaka0x0'

encrypted = binascii.a2b_hex('50523a0706580020004e334d6939314d6f5231587a49484e6652484e72746e5a304e47637a4e5862')


xored = [c1 ^ c2 for c1,c2 in itertools.zip_longest(map(int, key), map(int, encrypted), fillvalue=0)]
xored_str = bytes(bytearray(reversed(xored)))

print(base64.b64decode(xored_str).decode('ascii'))
