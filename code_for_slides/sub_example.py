import re

# Syntax: re.sub(regex, replacement_text, string_to_replace_text_in)
print re.sub(r'\bEdward|Ned|Eddie|Ed\b', r'Paul', 
    'Edward left. Ned came back in. Eddie asked, "Am I schizophrenic?" Ed said no.')

# 'Paul left. Paul came back in. Paul asked, "Am I schizophrenic?" Paul said no.'

