#! /usr/bin/env python

class DinnerError(Exception):
	pass

def makeDinner():
	userInput = raw_input("Please choose a dinner item: ")
	if userInput == "Ice cream":
		raise DinnerError("Not nutritious enough!!")
	if userInput == "computer":
		raise DinnerError("Not a dinner item")

try:
	makeDinner()
except Exception, explanation:
	print "Error,",explanation