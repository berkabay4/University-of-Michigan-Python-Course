# Create empty list
stuff = list()

# Print empty list
print('Before = ', stuff)

# Add some value in this list
stuff. append('book')
stuff.append(99)
stuff.append('cookie')
stuff.append(227.33)

print('After = ', stuff)

# Is Something in a List?
print('99 in this stuff list? Answer = ', 99 in stuff)
print('book in this stuff list? Answer = ', 'book' in stuff)
print('227 in this stuff list? Answer = ', 227 in stuff)


# A list can be sorted with sort() method
names = ['Gleen', 'Joseph', 'Bob', 'Isaac', 'Adrian', 'Sally']
numbers = [11,44,1,33,-8,12.66,44.2, -22.44]

print("Not Sorted ->", names)
print("Not Sorted ->", numbers)

# Sorted value in names list
names.sort()
# Sorted value in numbers list
numbers.sort()

print("Sorted ->", names)
print("Sorted ->", numbers)

