#!/usr/bin/python

import sys

totalSales = 0
numSales = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    _, thisSale = data_mapped
    thisSale = float(thisSale)

    totalSales += thisSale
    numSales += 1

print "total sales value: ", totalSales
print "number of sales: ", numSales

