#!/usr/bin/python

import os
import csv
import sys

from bottle import route, run, template

@route('/home')
def hello():
	reservations = os.popen("cat reservations.txt").read()
	return reservations	

run(host='localhost', port=8080, debug=True)
