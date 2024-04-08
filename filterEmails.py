import csv

buffer = ''
f =  open('rawEmails.txt', 'r', encoding='UTF-8')
r = open('cleanEmails.txt', 'w', encoding='UTF-8')

for line in f:
    for x in line :
        if x == ';':
            buffer += '\n'
        else:
            buffer += x
    print(buffer)
    r.write(buffer)


f.close