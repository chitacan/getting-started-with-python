#! /usr/bin/env python

from cgi import FieldStorage

form = FieldStorage()

print "Content-type: text/html"
print "Hello world from apache"
print form.getvalue('user')
print form.getvalue('email')