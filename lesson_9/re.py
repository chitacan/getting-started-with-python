#! /usr/bin/env python

import re

print re.search('a(.*)e', 'apple').group(1)
print re.findall('\w+@\w+\.com', 'email is chitacan@gmail.com wang_tai@gmal.com')