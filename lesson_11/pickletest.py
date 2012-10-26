#! /usr/bin/env python

import pickle

# oepn file or create if not exists
data = open('mydata.pkl', 'w')

# make some credential
cred = {"user":"jesse", "pass":"essej"}

# save credentail
pickle.dump(cred, data)
data.close()

# load saved data
data = open('mydata.pkl', 'r')
print pickle.load(data)
data.close()