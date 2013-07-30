# Exercise 4 - match prices $5.99 and less
# -----------------------------------------
import re

# Instructions: first, run this program from the command line
# You'll see that it fails the first test. Why? (Discuss.)

# Fix the regex so that it passes the first test. 
# Does it then pass the second test? If not, fix it again!

price_regex = r'$[0-5].\d\d' # match strings $0.00 to $5.99

if not re.match(price_regex, '$3.99'):
    print "Uh oh, it didn't match $3.99!"
elif re.match(price_regex, '$3999'):
    print "Uh oh, it matched $3999!"
else:
    print "Congratulations, you fixed it!"
