largest = -1
smallest = None
while True:
    num = input("Enter a number: ")

    try:
        fnum = float(num)
    except:
        if num == "done":
            break
        else:
            print("Invalid input")

    if smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum
    elif fnum > largest:
        largest = fnum


print("Maximum is", int(largest))
print("Minimum is", int(smallest))