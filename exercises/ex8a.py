# Exercise 8a

# Going back to the E-less book, write a function that takes a list of words
# and returns only those words that contain no E's.
# An outline of the function has been supplied for you.

import re
def remove_e_words(wordlist):
    non_e_words = list()
    for word in wordlist:
        if ...: # replace the ellipsis with your code
            non_e_words.append(word)
    return non_e_words

assert remove_e_words(['Acorn','Bread','Cornflakes','Dairy','Elephant ears']) \
    == ['Acorn', 'Dairy']

# Discuss: does it make sense to use re.match or re.search in this instance?
