# Looping Through Strings

# Using a while statement and a iteration variable,
# and the len function, we can construct a loop to
# look at each of the letters in a string individually

fruit = 'banana'
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

# With for loop
fruit_2 = 'pineapple'
for letter in fruit_2:
    print(letter)
