#! /usr/bin/env python

# kth h3 request script

import urllib
import urllib2
import ast

values = {
	"name":"",
	"email":"",
	"company":""
}

data = urllib.urlencode(values)

response = urllib2.urlopen("http://h3.kthcorp.com/2012/h3api/postReg", data, 10000)
result = ast.literal_eval(response.read())

print "code :",result['code']
print "code_text :",result['code_text']