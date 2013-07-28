# Exercise 1 - Using metacharacters

import re

# Match sequences that look like this: A1B C2D - pairs of letter-digit-letter sequences, separated by a space-lik character.
# Your regular expression should consist of a string of metacharacters.

regex  = r'...' # replace the ellipsis with a suitable regular expression

# What happens if we try to match a matching string?

string = 'A1b c2D' # you can change this around a little
print re.match(regex, string) 

# What happens if we try to match a non-matching string?

string = 'A1B_C2D' # you can change this around a little!
print re.match(regex, string)
