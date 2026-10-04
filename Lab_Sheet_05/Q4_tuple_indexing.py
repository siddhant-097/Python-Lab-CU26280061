# Access tuple elements using indexing

my_tuple = tuple(input("Enter tuple elements: ").split())

index = int(input("Enter index: "))

if -len(my_tuple) <= index < len(my_tuple):
    print("Element:", my_tuple[index])
else:
    print("Invalid index.")