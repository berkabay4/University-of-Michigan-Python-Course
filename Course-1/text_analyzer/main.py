#This part of the program shows a function that counts how many times a character occurs in a string.
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

# This function takes as its arguments the text of the file and one character, returning the number of times that character appears in the text.
# Now we can call it for our file.
filename = input("Enter a filename: ")  # Filename = test.txt
with open(filename) as f:
    text = f.read()
print("Count of a -> ", count_char(text,"a"))

# The next part of the program finds what percentage of the text each character of the alphabet occupies.
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))