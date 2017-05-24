c = "XkZDRgdBVUtpCRZoBkBRaFBoLANKWGx1Vl4EBhdFHmIwYWY4OTI2N2FmNTU4MzE2ZWY0MWQ1OGRjMGQ2MDlhMw==".decode('base64')
c2 = "3506d53009c722b7d7d0873690c2cdcb0af89267af558316ef41d58dc0d609a3"
s = ""
for i in range(len(c)):
    s += chr(ord(c[i]) ^ ord(c2[i]))

print s
    
