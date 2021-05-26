# String Functions

# find()

# We use the find() function to search
# for a suvstring within another string.

# find() finds the first occurrence of the substring
# If the substring is not found, find() returns "-1"

fruit = 'banana'
pos = fruit.find('na')
print(pos)

print(fruit.find('z'))

# Upper and Lower Case

greet = 'HELLO Bob'

# Make everything lower case
print(greet.lower())

# Make everything upper case
print('hello John!'.upper())

# Search and Replace

# The replace() function is like a "search and replace"
# operation in a word processor.

# It replaces all occurrences of the search string
# with the replacement string.

greet_2 = 'Hello Sarah'
nstr = greet_2.replace('Sarah', 'Jane') # replace(old,new)
print('1- Before =', greet_2)
print('1- After =',nstr)

nstr_2 = greet_2.replace('o','X')
print('2- Before =', greet_2)
print('2- After =', nstr_2)


# Stripping Whitespace

# Sometimes we want to take a string and remove
# whitespaces at the beginning and/or end

# lstrip() and rstrip() remove whitespace at
# the left or right

# strip() removes both beginning and ending whitespace

greet_3 = '    Hello Bob!    '
print("Normal ->", greet_3)
print("lstrip() ->", greet_3.lstrip())
print("rstrip() ->", greet_3.rstrip())
print("strip() ->", greet_3.strip())