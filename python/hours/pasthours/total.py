#!/usr/bin/python

# Hours python program

import os, sys, subprocess

total = 0
month = sys.argv[1]

with open(month) as f:
    for line in f:
        total = float(total) + float(line)

#confirm information is correct and send email
print 'Current hour total for the month %s' %  (total)

