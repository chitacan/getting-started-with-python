#! /usr/bin/env python

import sys

if len(sys.argv) > 1:
	defaultNum = int(sys.argv[1])
else:
	defaultNum = 5

def factorial(number):
	if (number == 1):
		return 1
	else:
		return number * factorial(number - 1)

print `defaultNum` + "! is",factorial(defaultNum)