#! /usr/bin/env python

def madlib(adjective='thirsty', name='adam'):
	print "the %s %s ate all the pizzas" % (adjective, name)

def shoppingCart(itemName, *prices):
	for price in prices:
		print 'price :',price

def shoppingCart(itemName, **prices):
	for price in prices:
		print price, ':', prices[price]

def shoppingCart(itemName, prices):
	print 'item:',itemName
	for price in prices:
		print price, ':', prices[price]

def dbLookup():
	dict = {}
	dict['amazon'] = 100
	dict['ebay'] = 120
	dict['bestbuy'] = 140
	return dict;

# madlib('hungry', 'jeffrey')
# madlib()
# shoppingCart('laptop', 100, 170, 32)
# shoppingCart('laptop', amazon=100, ebay=170, bestbuy=32)

shoppingCart('laptop', dbLookup())