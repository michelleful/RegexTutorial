import re
from test_regex import test_regex

# ---------------
#  Exercise 6a
# ---------------

# Write a regex that matches the words bad, baad, baaad 
# for any arbitrary number of a's

animal_farm_bleat_regex = r'...' # replace the ellipsis with your regex

test_regex('Animal farm bleat', animal_farm_bleat_regex, 
    ['baaaaaaad', 'This is baaaaaaaaaaad!'],  # should match these
    ['bd', 'bacd', 'baaaaa', 'sinbaaaad'])    # shouldn't match these
    

# ---------------
# Exercise 6b
# ---------------

# Write a regex that matches the word baaad (3 a's) up to baaaaaaaaaad (10 a's).

animal_farm_short_bleat_regex = r'...'

test_regex('Animal farm short bleat', animal_farm_short_bleat_regex, 
    ['baaaaaaad', 'This is baaaaaaaaaad!'], # should match these
    ['bd', 'bacd', 'baaaaa', 'sinbaaaad', 'baad', 'baaaaaaaaaaaad']) # not these


# ---------------
# Exercise 6c
# ---------------

# Write a regex that matches both the strings 'homebrew' and 'home-brew'

homebrew_regex = r'...'
test_regex('Homebrew regex', homebrew_regex, 
    ['homebrew', 'home-brew'], # should match these
    ['home brew']) # shouldn't match these
    


# ---------------
#  Exercise 6d
# ---------------

# Following in the footsteps of Ernest Wright Homer, you're writing a 
# book with no E's. That's right, you can't even use the word 'the'. 

# You decide to filter your wordlist so it contains only words with no E's. 
# Write a regular expression to filter the dictionary.

no_e_regex = r'^...$' # replace the ellipsis with a regex 
                      # that matches only strings without E's. 
                      # Spaces are acceptable.
test_regex('No E regex', no_e_regex, 
    ['Brobdingnagian', 'ginormous'], 
    ['never', 'what never?', 'no never', 'Elephant'])

# Discuss: why can't we use a regex without the +/*?


# ---------------
#  Exercise 6e
# ---------------

# Look at regex 1 and regex 2 defined below. How much of ab_string 
# do you think they will match?

regex1 = r'(ab)*'
regex2 = r'ab*'
ab_string = 'ababababa'

# my guess for regex 1:
# my guess for regex 2: 

print re.match(regex1, ab_string).group(0)
print re.match(regex2, ab_string).group(0)

# You can also match repetitions of multiple characters 
# using open and close brackets
