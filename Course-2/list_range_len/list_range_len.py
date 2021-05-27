# Using the range function

# The range function returns a list of numbers
# that range from zero to one less than the parameter.

# We can construct an index loop using for and an
# integer iterator

friends = ['Bob', 'Joseph', 'Glenn']
friends_2 = ['Saul', 'Paul', 'Janna']
print("Lenght = ", len(friends))

print(range(len(friends)))


for friends in friends:
    print('1- Happy New Year', friends)

# We can also use for loop with range-len functions
for i in range(len(friends_2)):
    print('2- Happy New Year', friends_2[i])
