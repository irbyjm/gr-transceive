#!/usr/bin/env python
# 201711125 irbyjm

# import sys to have command line argument for file name
# import binascii to easily convert between hexadecimal, ASCII, and binary
import sys
import binascii

# make sure a filename is specified else dump usage text
if len(sys.argv) == 1:
    print("Usage: ./fix_decode.py [file]")

else:
    # open desired file for reading into readfile
    readfile = open(sys.argv[1], "rb")

    # open new file to dump fixed data into
    outfile = open(sys.argv[1]+".fixed", "wb")

    # read entire input file into hexin (it will be all hex)
    hexin = readfile.read()

    # convert this massive hex string into integer and then binary
    # strip '0b' binary indicator from the front for further processing
    binary_string = bin(int(binascii.hexlify(hexin), 16))[2:].zfill(8)

    # split the giant binary string into multiple pieces with framing tag
    # '01111110' as separator between transmissions. this framing tag is
    # hard-coded into transmitter input vector
    for line in binary_string.split('01111110'):

        # make sure each line is some multiple of 8 bits long otherwise
        # there are missing or extra bits which won't be able to decode
        if len(line) % 8 == 0 and len(line) != 0:

            # pad the binary indicator '0b' back onto the data
            newline = int('0b'+line, 2)

            try:

                # write the binary into the new file
                outfile.write(binascii.unhexlify('%x' % newline))
            except:

                # do nothing?
                True

    # housecleaning!
    readfile.close()
    outfile.close()
