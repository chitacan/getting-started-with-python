#! /usr/bin/env python

# read file
# file = open('test.txt', 'r')

# file.read()

# for line in file.readlines():
# 	print line

# write file
# file = open('test.txt', 'w')

# append file
# file = open('test.txt', 'a')
# file.write('this is at the end of test.txt')

# read & write file in binary mode
# file = open('test.txt', 'r+b')

with open('test.txt') as file:
	print file.read()