# Exercise 10

# Write a regular expression for finding adverbs (ending in -ly) 
# and use it in the find_adverbs() function to find all the adverbs 
# in a sentence.

import re

adverb_regex = r'\b(\w+ly)\b' # replace the ellipsis with your regular expression
def find_adverbs(sentence):
    """Returns a list of adverbs in the supplied sentence"""
    return re.findall(adverb_regex, sentence) # replace this with your code

extremely_bad_writing = """Mary swooned breathlessly when her paramour 
entered the room speedily, relying greatly on his eagle eyes to find his 
lady-love lying on the bed."""

try:
    assert find_adverbs(extremely_bad_writing) == \
                    ['breathlessly', 'speedily', 'greatly']
    print "Yay it worked"
except:
    print "Got the wrong set: ", find_adverbs(extremely_bad_writing)
