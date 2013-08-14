import re

name_regex = r'\b([A-Z][a-z]+)\b \b([A-Z][a-z]+)\b'
# Note:this is a TERRIBLE way to check for names. Why?
m = re.search(name_regex, '"Oliver Twist" was written by Charles Dickens')
if m:
    print m.groups()
    
# returns ('Oliver', 'Twist')

