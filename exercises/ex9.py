# Exercise 9

# Write a regular expression to capture all email addresses that have the form 
# ...@pyladies.org
# Furthermore we just want to capture the username BEFORE the @.

import re

pyladies_regex = r'(\S+)\@pyladies\.org' # replace the ellipsis with your email address

# Then use it to capture email addresses from the following list of records
# disclaimer: not actual email addresses :P
our_members = """
Jennifer jennifer@pyladies.org
Margaret margaret@pyladies.org
Michelle michelle@pyladies.org 
"""

# your code here
for record in our_members.split('\n'):
    m = re.search(pyladies_regex, record) # put your code here
    if re.search(pyladies_regex, record):
        print m.group(1)
