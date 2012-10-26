#! /usr/bin/env python

from bs4 import BeautifulSoup
from urllib import urlopen

html = urlopen("http://litemind.com/best-famous-quotes/").read()

soup = BeautifulSoup(html)

for section in soup.findAll('div', {"class":"wp_quotepage"}):
	quote  = section.findChildren()[0].renderContents()
	author = section.findChildren()[1].renderContents()

	print quote, author