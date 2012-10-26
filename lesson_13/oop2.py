#! /usr/bin/env python

class house:

	def __init__(self, doors=3):
		self.doors = doors

	def slamDoors(self):
		for door in range(self.doors):
			print "SLAM!!"

class castle(house):

	def fireCannons(self, number):
		for cannon in range(number):
			print "fire",cannon,"boom!"

	def payMortgage(self):
		print "ready  the cannons"

class apartment(house):

	def payMortgage(self):
		print "here is your money"

landlordsProperties = [castle(), apartment()]

for house in landlordsProperties:
	house.payMortgage()