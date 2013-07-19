import re

product_code_regex = re.compile(r'[A-Z]\d{3}')
print type(product_code_regex) 
# <type '_sre.SRE_Pattern'>

print product_code_regex.findall('A103 B296 Z999') 
# ['A103', 'B296', 'Z999']

# This is equivalent to:
print re.findall(r'[A-Z]\d{3}', 'A103 B296 Z999') 
# ['A103', 'B296', 'Z999']

