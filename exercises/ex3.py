# Exercise 3 - examples with ^, $, \b

# Go through each line and predict whether there will be a match or not. 
# Then run this program and see whether you were right.

import re

print "Match 1: ", re.search(r'^Hallo$', 'Hallo')        # Matches: yes
print "Match 2: ", re.search(r'^Hallo$', 'Hallo World')  # Matches: no
print "Match 3: ", re.search(r'^Hallo$', 'Well, Hallo!') # Matches: no

print "Match 4: ", re.search(r'\bHallo\b', 'Well, Hallo!') # Matches: yes
print "Match 5: ", re.search(r'\bHallo\b', 'Harry Potter and the Deathly Hallows') # Matches: no
