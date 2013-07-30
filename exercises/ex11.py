# Exercise 11

# Earlier, we defined a regex to find email addresses.
# Try putting capturing parentheses around the whole thing
# and examine the match object that results

# Instructions: in the regex below, 
# place capturing parentheses in the appropriate place
email_regex = r'\w+@\w+\.(com|org|edu|net)' 
m = re.search(email_regex, 'My email is amy@gmail.com')
print m.groups() 

# Discuss: why is the output of this command what it is?
# Go back and fix the regex so that only the email address is captured

