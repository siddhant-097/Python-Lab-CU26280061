# Remove an element using remove()

my_set = {10, 20, 30, 40}

element = int(input("Enter element to remove: "))

if element in my_set:
    my_set.remove(element)
    print("Updated set:", my_set)
else:
    print("Element not found.")