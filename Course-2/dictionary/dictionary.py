
# When we encounter a new name, we need to add a new
# entry in the dictionary and if this the second or
# later time we have seen the name, we simply
# add one to the count in the dictionary under that name

# Create empty dictionary
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# Simplified counting with get()

# We can use get() and provide a default value of zero
# when the key is not yet in the dictionary - and then just add one

counts2 = dict()
names2 = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name2 in names2:
    counts2[name2] = counts2.get(name2, 0) + 1
print(counts2)