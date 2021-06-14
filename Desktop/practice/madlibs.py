

sentence = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events"
lists = sentence.split()
print(lists)

for list in range(len(lists)):
    if lists[list] == 'ADJECTIVE':
        adjective = input('Enter the adjective : ')
        lists[list] = adjective
    elif lists[list] == 'NOUN':
        noun = input('Enter the noun : ')
        lists[list] = noun
    elif lists[list] == 'VERB.':
        verb = input('Enter the verb : ')
        lists[list] = verb

sentence = ""
for list in lists:
    sentence += '  ' + list
print(sentence)
