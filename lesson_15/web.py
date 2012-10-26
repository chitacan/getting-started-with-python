#! /usr/bin/env python

# download image from web site
# import urllib
# urllib.urlretrieve("http://jshawl.com/python-playground/python.gif", "python.gif")

# parse email from site
# import urllib
# import re
# html = urllib.urlopen("http://jshawl.com/python-playground/")
# print re.findall('[\w.]+@[\w.]+', html.read())

import urllib
import urllib2
from cookielib import CookieJar

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())

formValues = {
	"username":"user",
	"password":"pass"
}

data = urllib.urlencode(formValues)

response = opener.open("http://jshawl.com/python-playground/login.php", data)

# print response.read()

secure = opener.open("http://jshawl.com/python-playground/protected2.php")

print secure.read()