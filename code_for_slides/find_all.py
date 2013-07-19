import re

name_regex = r'\b([A-Z][a-z]+)\b \b([A-Z][a-z]+)\b'
print re.findall(name_regex, '"Oliver Twist" was written by Charles Dickens')
    
# returns [('Oliver','Twist'), ('Charles','Dickens')]

