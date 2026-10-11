# Check whether an element exists in a set

my_set = {10, 20, 30, 40}

element = int(input("Enter element to search: "))

if element in my_set:
    print("Element exists in the set.")
else:
    print("Element does not exist.")