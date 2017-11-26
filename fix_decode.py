#!/usr/bin/env python

import sys
import binascii

readfile = open(sys.argv[1], "rb")
outfile = open(sys.argv[1]+".fixed", "wb")

hexin = readfile.read()
binary_string = bin(int(binascii.hexlify(hexin), 16))[2:].zfill(8)

for line in binary_string.split('01111110'):
    if len(line) % 8 == 0:
        newline = int('0b'+line, 2)
        outfile.write(binascii.unhexlify('%x' % newline))

readfile.close()
outfile.close()
