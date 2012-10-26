#! /usr/bin/env python

class house:

	__cost = 1200

	doors = 10

	def addDoors(self, number):
		self.doors = number

	def slamDoors(self):
		for door in range(self.doors):
			print "SLAM!"
		print "cost for house",self.__cost

myhouse = house()
myhouse.slamDoors()
