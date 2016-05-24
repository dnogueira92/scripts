#!/usr/bin/python

import os
import csv
import sys

from bottle import route, run, template

@route('/home')
def hello():
	
	

	#reservation = os.popen("scontrol show reservations -o).read()
	reservation = os.popen("cat reservations.txt").read()
	
	return template('test', reservation=reservation)
	

run(host='localhost', port=8080, debug=True)
