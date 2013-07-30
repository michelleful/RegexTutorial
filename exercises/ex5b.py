# Exercise 5b - Set complements

# You're processing some DNA sequences and you notice that some of them 
# have been corrupted - they contain letters other than A,T,C and G! 
# Write a regex that will let you remove the corrupted sequences.

not_dna_regex = r'...' # replace ellipsis with a regex that matches 
                       # sequences that contain anything other than A, T, C & G
test_regex('Not DNA regex', not_dna_regex, 
    ['ATCHGA', '#*@!'], ['AGGGGGCTAA', 'ACGAT'])

# Notice that your regex matches non-alphabetic characters as well!
