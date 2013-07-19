import re

email_at = r'(\w+)@(\w+\.(?:com|net|edu|gov))'
print re.sub(email_at, r'\1 (at) \2', 'amy@gmail.com')
# 'amy (at) gmail.com'
print re.sub(email_at, r' (at) ', '@amy')
# '@amy'
