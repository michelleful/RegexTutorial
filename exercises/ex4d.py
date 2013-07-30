# The purpose of this exercise is to illustrate that metacharacters
# retain their regular meaning within character sets []

import re
from test_regex import test_regex

# Instructions: read the regex, and run the code to verify that
# it does indeed match the literal characters $, ^ and .

metacharacter_regex = r'[$^.]'

# Test regex to make sure it matches '^','$','.' and not 'a' or '1'.
test_regex('Metacharacter regex', metacharacter_regex, '^$.', 'a1')
