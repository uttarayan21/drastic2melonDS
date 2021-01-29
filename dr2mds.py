#!/usr/bin/python3

from math import log
import os

DRASTIC_SAVE="Pokemon Black.dsv"
MELONDS_SAVE="Pokemon Black.sav"

def st_size(path):
    return os.stat(path).st_size

def closest2pow(n):
    return 2**int(log(n) / log(2))

def drastic2melonds(infile,outfile):
    with open(infile,"rb") as inf, open(outfile,"wb") as ouf:
        
        ouf.write(inf.read(closest2pow(st_size(infile))))

if __name__ == "__main__":
    drastic2melonds(DRASTIC_SAVE,MELONDS_SAVE)
