#!/usr/bin/env python
#20171125 irbyjm

# import sys to pass filename via command line argument
# import binascii to easily convert between ascii, hexacedimal, and binary
import sys
import binascii

# if script is ran without filename argument dump the usage line
# it should work with absolute or relative pathing
if len(sys.argv) == 1:
    print("Usage: ./fix_decode.py [file]")
else:

    # open the file from command line argument for reading
    # open a new file for writing fixed data
    readfile = open(sys.argv[1], "rb")
    outfile = open(sys.argv[1]+".fixed", "wb")

    # read the entire binary file into hexin variable
    hexin = readfile.read()

    # convert hexin into an integer value and then convert to binary
    # [2:] removes the leading '0b' and zfill pads any missing bits
    binary_string = bin(int(binascii.hexlify(hexin), 16))[2:].zfill(8)

    # go through binary_string and split it into a multi-value array delimited
    # by the header flag '01111110' hard-coded into transmitter
    for line in binary_string.split('01111110'):

        # if the length of the line is not divisible by 8 some bits missing
        if len(line) % 8 == 0:

            # slap '0b' back onto the binary to make the variable a binary num
            newline = int('0b'+line, 2)

            # use binascii to write the binary value as ASCII in output file
            outfile.write(binascii.unhexlify('%x' % newline))

            # housecleaning!
            readfile.close()
            outfile.close()
