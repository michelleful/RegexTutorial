# Exercise 7

import re
from test_regex import test_regex

# Write a regex that matches filenames ending in .doc and .odt

word_file_regex = r'...'

test_regex('Word file regex', word_file_regex, 
    ['math_girls.doc', 'mathgirls2.odt'], 
    ['other.ddt', 'odt'])
