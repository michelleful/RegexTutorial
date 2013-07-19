# code from the Python docs
m = re.match(r"(?P<first_name>\w+) 
               (?P<last_name>\w+)", 
               "Malcolm Reynolds")
m.group('first_name') # 'Malcolm'
m.group('last_name')  # 'Reynolds'
