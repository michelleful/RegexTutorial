# Exercise 4a - match prices $5.99 and less

import re

price_regex = r'$[0-5].\d\d' # match strings $0.00 to $5.99

if not re.match(price_regex, '$3.99'):
   print "Uh oh, it didn't match!"

# Why doesn't this work?

# Exercise 4b - fixing price regex

# Fix the price_regex below and try running this code block

price_regex = r'$[0-5].\d\d' # match strings $0.00 to $5.99

if not re.match(price_regex, '$3.99'):
    print "Uh oh, it didn't match!"
    
if re.match(price_regex, '$3999'):
    print "Uh oh, it matched $3999!"

# Exercise 4c - fixing price regex

# Fix the price_regex below and try running the code block (note: you'll have to fix two things!)

price_regex = r'$[0-5].\d\d' # match strings $0.00 to $5.99

if not re.match(price_regex, '$3.99'):
    print "Uh oh, it didn't match!"
    
if re.match(price_regex, '$3999'):
    print "Uh oh, it matched $3999!"
