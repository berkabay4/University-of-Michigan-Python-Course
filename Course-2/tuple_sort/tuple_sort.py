# Sort by key
d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
print(t)

for k,v in t:
    print(k,v)

# Sort by values instead of key

# If we could construct a list of tuples
# of the from (value, key) we could sort by value

# We do this with a for loop that creates a list of tuples

c = {'a':122, 'b': 22, 'c': 35, 'd':-77}
tmp = list()

for k,v in c.items():
    tmp.append((v,k))
print("Not Sorted -> ", tmp)

tmp = sorted(tmp, reverse= True)
print("Sorted -> ", tmp)