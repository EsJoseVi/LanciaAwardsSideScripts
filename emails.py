buffer = ''
f =  open('cleanEmails.txt', 'r', encoding='UTF-8')
r = open('emails.txt', 'w', encoding='UTF-8')

for line in f:
    start = False
    for x in line :
        if x != '>':
            if start:
                buffer += x
            if x == '<':
                start = True
print(buffer)
r.write(buffer)


f.close