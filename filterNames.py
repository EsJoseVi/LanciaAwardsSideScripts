import csv

names = open("rawNames.txt", 'r', encoding='UTF-8')

list = list()

for line in names:
    buffer = ''
    for i in line:
        if i.isalpha() or i.isspace():
            buffer += i
        else:
            break
    list.append(buffer)
print(list[1])
print(len(list))

with open('names.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(list)):
        writer.writerow({'name' : list[i]})