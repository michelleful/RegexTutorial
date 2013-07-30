# Exercise 5a - Set complements

# Let's rearrange the metacharacter_regex from Exercise 4d. 
# Why doesn't it work as we wanted?

metacharacter_regex = r'[^$.]'
test_regex('Metacharacter regex', metacharacter_regex, '^$.', 'a1')

# Edit the metacharacter regex below to make it work,
# in some way OTHER than rearranging the characters again

edited_metacharacter_regex = r'[^$.]'
test_regex('Edited Metacharacter regex', edited_metacharacter_regex, '^$.', 'a1')

# So, saying "within character sets [], metacharacters have their 
# regular meaning except backslashes" is true EXCEPT that 
# ^ means complement if it's the first character [^...]. 
# Elsewhere, it means the caret character.
