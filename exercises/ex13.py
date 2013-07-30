# Exercise 13

# You've been sent a script by a Japanese writer who, following Japanese 
# naming conventions, has put the last name before the first name everywhere. 

# Locate all the lastname-firstname pairs in the script
# and reorder them according to Western naming conventions. 
# The regex has been supplied to you.

name_regex = r'\b([A-Z][a-z]+)\b \b([A-Z][a-z]+)\b'

script = """This scene has Mukai Miruka teaching Suzuki Tetra, 
            Toru Yuri, and the unnamed narrator about Fermat's last theorem."""

# replace the ellipsis with the appropriate substitution string
westernised_script = re.sub(name_regex, ..., script) 
print westernised_script
