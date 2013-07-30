# Exercise 12

# Use the email regex to replace all email addresses with (email redacted).

email_regex = r'\w+@\w+\.(com|org|edu|net)'
text_to_be_redacted = '''Amy doesn't want the whole world to see 
                         that her email is amy@gmail.com. 
                         Or that her backup email is amy@yahoo.com'''

def redact_email(text):
    return ... # replace the ellipsis with your code

print redact_email(text_to_be_redacted)
