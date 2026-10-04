# Check whether an element exists in a tuple

my_tuple = tuple(input("Enter tuple elements: ").split())

element = input("Enter element to search: ")

if element in my_tuple:
    print("Element exists in the tuple.")
else:
    print("Element does not exist.")