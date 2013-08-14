# Exercise 1 - Using metacharacters

import re

# Match sequences that look like this: A1b c2D - pairs of letter-digit-letter sequences, separated by a space-lik character.
# Your regular expression should consist of a string of metacharacters.

regex  = r'...' # replace the ellipsis with a suitable regular expression

# Then run the script and look at the output of the print statements below.

# What happens if we try to match a matching string?
string = 'A1b c2D'
print re.match(regex, string)

# What happens if we try to match a non-matching string?
string = 'A1b_C2D'
print re.match(regex, string)


