name = input("Enter file:")
hande = open(name)

counts = dict()
for line in hande:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount
        bigword = word
        bigcount = count