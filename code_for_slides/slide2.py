import string
for line in open('purchaserecords.txt','r'):
    if line[0] in string.uppercase and \
       line[1].isdigit() and \
       line[2].isdigit() and \
       line[3].isdigit():
        print line
    else:
        continue
