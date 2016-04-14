#!/usr/bin/python

import os
import csv
import sys

from bottle import route, run, template

@route('/home')
def hello():
	
	

	#reservations = os.popen("scontrol show reservations -o).read()
	reser = os.popen("cat reservations.txt").read()

	res = reser.split()

	
	return template('test', res=res)
	

run(host='localhost', port=8080, debug=True)
