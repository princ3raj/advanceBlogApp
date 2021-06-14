

file = open('index.html')
items = file.readlines()

for i in items:
    if 'educative' not in i:
        items.remove(i)

print(items)


newFile = open('new.html', 'w')

for item in items:

    newFile.write(item)
file.close()
newFile.close()
