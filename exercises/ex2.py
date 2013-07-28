# Exercise 2 - Specifying custom sets of characters

# We saw some metacharacters in the previous slide: \w, \d, \s
# Define custom character ranges that are equivalent to these, 
# WITHOUT using metacharacters (escape sequences like \n are fine)

# Exercise 2a
digit_regex     = r'[...]' # match definition of \d

# Exercise 2b
wordlike_regex  = r'[...]' # match definition of \w (at least, for English)

# Exercise 2c
spacelike_regex = r'[...]' # match definition of \s

# No need to edit below this point. Run this program to see if your answers were correct.
from test_regex import test_regex
test_regex('Digit regex', digit_regex, '0123456789', 'aZ \t\n$_')
test_regex('Wordlike regex', wordlike_regex, 'ampBLY_058', ' \t\n-$')
test_regex('Spacelike regex', spacelike_regex, ' \t\r\n', 'ahlB_-$9')
