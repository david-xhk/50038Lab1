#!/usr/bin/python

import sys

currentIp = None
numHits = 0

for line in sys.stdin:
    thisIp = line.strip()
    
    if currentIp and thisIp != currentIp:
        print currentIp, "\t", numHits
        currentIp = thisIp
        numHits = 0
    
    currentIp = thisIp
    numHits += 1

if currentIp:
    print currentIp, "\t", numHits
