#! /usr/bin/env python

# Setup new lesson folder and file for "Getting Started with Python" course.

import sys
import subprocess as sp

def printUsage():
	print "Usage : setup [directory] [file] [options]"

def printResult(dirName, fileName):
	print "Setup Complete : in directory " + dirName + ", " + fileName

def callWithMsg(arguments, msg=""):
	result = sp.call(arguments)

	if len(msg) != 0:
		print msg

	if result > 0:
		sys.exit(0)

def makeFileName():
	if len(sys.argv) < 3:
		return 'touch.py'
	else:
		return sys.argv[2]

# TODO : print error message with red color
if len(sys.argv) == 1:
	print "failed : wrong arguments"
	printUsage()
	sys.exit(0)

dirName = sys.argv[1]
fileName = dirName + '/' + makeFileName()

callWithMsg(['mkdir', dirName])
callWithMsg(['touch', fileName])
callWithMsg(['chmod', '+x', fileName])

f = open(fileName, 'w')
f.write('#! /usr/bin/env python')
f.close()

printResult(dirName, fileName)