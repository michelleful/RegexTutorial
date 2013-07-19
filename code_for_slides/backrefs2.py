import re

print re.sub(r'(\b\S+\b) \1', r'\1', 
    'This is is a string with doubled doubled words')
# 'This is a string with doubled words'

