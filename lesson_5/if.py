#! /usr/bin/env python

name = raw_input('please type in your name : ')

if len(name) < 5:
	print "your name is fewer than 5 chars"
elif len(name) == 5:
	print "your name is exactly 5 chars"
else:
	print "your name is greater than 5 chars"