# Exercise 8b

import re

# You want to filter a list of strings for those containing valid email addresses.
# First write a regular expression that checks for a string containing:
# (1) some alphanumeric stuff
# (2) @ sign
# (3) domain name (alphanumeric)
# (4) .com, .org, .edu or .net (Okay, this isn't all valid email addresses)

email_regex = r'...' # replace this with your regex

# Now replace the ellipsis in the code below with some Python code
# that refers to email_regex 

def filter_lines_with_email(list_of_lines):
    filtered_lines = list()
    for line in list_of_lines:
        if ...: # replace ellipsis with your code
            filtered_lines.append(line)
    return filtered_lines

line0 = 'This line contains a valid email address amy@gmail.com'
line1 = 'This isn\'t a valid email: @gmail.com'
line2 = 'You can contact me at maf@mit.edu, anytime'
line3 = 'If you tried to send an email to @@(@$@gmail.com I\'m sure it would be rejected'

assert filter_lines_with_email([line0, line1, line2, line3]) == [line0, line2]
