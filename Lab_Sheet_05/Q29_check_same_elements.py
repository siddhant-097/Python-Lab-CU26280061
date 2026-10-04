# Check whether all tuple elements are the same

my_tuple = tuple(input("Enter tuple elements: ").split())

if len(my_tuple) == 0:
    print("Tuple is empty.")
elif all(item == my_tuple[0] for item in my_tuple):
    print("All elements are the same.")
else:
    print("All elements are not the same.")