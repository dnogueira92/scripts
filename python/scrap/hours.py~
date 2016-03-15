#!/usr/bin/python

# Hours python program

import os, sys, subprocess
from datetime import datetime
now = datetime.now()

#constants
day = now.strftime("%Y-%m-%d")
total = 0

#variables
time_in = sys.argv[1]
time_out = sys.argv[2]
work = sys.argv[3]

#functions
def convert(x):
	(h, m) = x.split(':')
	h = float(h)
	m = float(m)
	
	if m <= 7:
		m = .00
	elif m <=22:
		m = .25
	elif m <= 37:
		m = .50
	elif m <= 52:
		m = .75
	else:
		m = 1.00

	return h + m

def append_file(today):
	f = open("total.txt", 'a')
	f.write('%s \n' % (today))
	f.close
	
#total hours
itime_in = convert(time_in)
itime_out = convert(time_out)
today = itime_out - itime_in

#append log and add hours
print today
append = raw_input("Would you like to add these hours to the log?(Y/N) ")

if append = "":
	append = 'y'

if append is 'y' or append is 'Y':
	append_file(str(today))

with open('total.txt') as f:
    for line in f:
        total = float(total) + float(line)

#confirm information is correct and send email
subject = 'Hours for %s - %s' %  (day, total)

table = 'dnogueira|%s|%s|%s|%s|%s|MGHPCC/INTERN|Y|N|%s' % (day, time_in, day, time_out, today, work)

print subject + '\n'
print table + '\n'

send = raw_input("Would you like to send this?(Y/N) ")

if append = "":
	append = 'y'

if send is 'y' or send is 'Y':
	command_line = 'echo -e "%s" | mail -s "%s" sb@techsquare.com' % (table, subject)
	subprocess.call(command_line, shell=True)
