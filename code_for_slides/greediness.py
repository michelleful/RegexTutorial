import re

# Default greedy matching
m = re.match(r'(ab+)', 'abbbbbbbb')
print m.groups() # ('abbbbbbbb',)

# Non-greedy matching with ?
m = re.match(r'(ab+?)', 'abbbbbbbb')
print m.groups() # ('ab',)


