# Helper function for testing your regexes to check that they work

import re 

def test_regex(regex_name, regex, successful_cases, unsuccessful_cases):
    cregex = re.compile(regex)
    errors = 0
    for case in successful_cases:
        if not cregex.search(case):
            print "Your %s didn't match %s" % (regex_name, case)
            errors += 1
    for case in unsuccessful_cases:
        if cregex.search(case):
            print "Your %s matched %s when it wasn't supposed to" % (regex_name, case)
            errors += 1
    if errors == 0:
        print "No errors in your %s" % regex_name
