# Find the index of an element

my_tuple = tuple(input("Enter tuple elements: ").split())

element = input("Enter element to find: ")

if element in my_tuple:
    print("Index:", my_tuple.index(element))
else:
    print("Element not found.")