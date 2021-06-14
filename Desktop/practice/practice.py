import re
import os
import shelve
PhoneNumRegx = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
mo = PhoneNumRegx.search('123-123-1234')
print(mo.group())


PhoneNUmRegxGroup = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = PhoneNUmRegxGroup.search('My Phone number is 123-123-1234')
print(mo1.groups())
print(mo1.group(1))
print(mo1.group(2))


heroRegx = re.compile(r'Bat(man|mobile|copter)')
hero = heroRegx.search('My Name is Batman')
print(hero.group())
print(hero.group(1))
print(hero.groups())


batRegx = re.compile(r'Bat(wo)?man')
bat = batRegx.search('The Adventures of Batman')
print(bat.group())


# Regx for asterisk zero or more occurences

# Regx for plus works same as well but for one or more occurences

astBat = re.compile(r'Bat(wo)*man')
ast = astBat.search('Batwowowowoman')
print(ast.groups())
print(ast.group())


# Matching Specific Repetitions with Curly Brackets

repetition = re.compile(r'(ha){3}')
rep = repetition.search('hahaha')
print(rep.group())


repetition_with_range = re.compile(r'(ha){3,5}')
rep_range = repetition_with_range.search('hahahaha')
print(rep_range.group())

rep_range = repetition_with_range.search('hahahahaha')
print(rep_range.group())

repetition_with_range_tweaks = re.compile(r'(ha){3,}')
# match three or more
repetition_with_range_tweaks_two = re.compile(r'(ha){,5}')
# match zero to five instances


# Greedy and Nongreedy Matching

# matches the largest string possible
greedyRegx = re.compile(r'(ha){3,5}')
greedy_one = greedyRegx.search('hahahahaha')
print(greedy_one.group())


# matches the shortest string possible
noneGreedyRegx = re.compile(r'(ha){3,5}?')
non_greedy = noneGreedyRegx.search('hahahahaha')
print(non_greedy.group())

# findall() method with no groups returns a list

PhoneNumRegx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone = PhoneNumRegx.findall('123-124-1245 and prince 123-678-3455')
print(phone)

# findall() method with groups returns a tuple.
#  in this case it'll return list of tuples because you have more than one matching
PhoneNUmRegxGroup = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phone_group = PhoneNUmRegxGroup.findall(
    '999-123-1234 and the only thing is 123-654-1234')
print(phone_group)


# Character Class

# /D any character excepts from 0-9

character = re.compile(r'\D*')
character_one = character.findall('prince&%# is a good guy')
print(character_one)

# /w Any letter, numeric digit or the underscore character
character_w = re.compile(r'\w+')
character_w_one = character_w.findall('a_b c 1 2 3')
print(character_w_one)

character_w_two = character_w.search('a_b c 1 2 3')
print(character_w_two.group())

# \W Any character that is not a letter, numeric digit, or the underscore character

# \s Any space, tab, or newline character. (Think of this as matching “space” characters.
space_characters = re.compile(r'\s{3,5}')

space = space_characters.findall('      and      ')
print(space)


# example

xmasRegx = re.compile('\d+\s\w+')
xmasRegx_one = xmasRegx.findall(
    '12 Birds 14 Cage 67 Princy No Birds 134 toolz'
)
print(xmasRegx_one)


# Note that inside the square brackets, the normal regular expression
# symbols are not interpreted as such. This means you do not need to escape
# the ., *, ?, or () characters with a preceding backslash. For example, the
# character class [0-5.] will match digits 0 to 5 and a period. You do not need
# to write it as [0-5\.].


# making your own character class

vowelRegX = re.compile(r'[aeiouAEIOU]')
vowel = vowelRegX.findall('boy name is good but DO You Have ANy Umbrella')
print(vowel)

allChars = re.compile(r'[A-Z]')
allchars = allChars.findall('abc abc abc Z 1')
print(allchars)

# caret character (^) will onlymatch those characters which are not in charcter class

consonRegx = re.compile(r'[^aeiouAEIOU]')
consonant = consonRegx.findall('prince raj')
print(consonant)


print(os.getcwd())
os.chdir('/Users/princeraj/')

print(os.getcwd())


totalSize = 0


for filename in os.listdir('Desktop'):
    print(filename)

    print(os.path.getsize(os.path.join('Desktop', filename)))

shelfFile = shelve.open('index')
cats = ['a', 'b', 'c']
shelfFile['cats'] = cats
shelfFile.close()

shelf = shelve.open('index')
print(shelf['cats'])
shelf.close()
