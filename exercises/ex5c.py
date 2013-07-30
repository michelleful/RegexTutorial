# Exercise 5c - Set complements

# You're looking at a list of purchases again. 
# Acme company uses product codes with A,B,C followed by three digits.
# Axeme company uses product codes X,Y,Z followed by three digits.

# Write a regex to extract lines with just Acme and Axeme's product codes, 
# *using a set complement* rather than r'[ABCXYZ]...'

# Also, make sure that the product code occurs at the *end* of the line

acme_axeme_regex = r'...' # replace the ellipsis with your regex

# No need to edit below this line
matches = ['This line contains Acme product code C180', 
           'This line contains Axeme product X007']
nonmatches = ['This line contains Hugo\'s product code J982',
              'This line contains an incorrect Axeme product code Z48A',
              'This line contains Acme code C180 but it\'s not at the end.']
test_regex('Acme/Axeme regex', acme_axeme_regex, matches, nonmatches)

# Notice that we did something a bit dangerous here - 
# the regex also matches product codes like '0000'.
# So, be careful when using set complements!

