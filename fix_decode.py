#!/usr/bin/env python

import sys
import binascii

readfile = open(sys.argv[1], "rb")
outfile = open("outfile", "wb")

hexin = readfile.read()
binary_string = bin(int(binascii.hexlify(hexin), 16))#[2:].zfill(8)

for line in binary_string.split('01111110'):
    if len(line) % 8 == 0:
        outfile.write(hex(int('0b'+line), 2))
# output file should have line by line of "good decodes" or at least full-length 8-bit modulo decodes

readfile.close()
outfile.close()
