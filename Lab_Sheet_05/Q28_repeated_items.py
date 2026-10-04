# Find repeated items in a tuple

my_tuple = tuple(input("Enter tuple elements: ").split())

repeated = ()

for item in my_tuple:
    if my_tuple.count(item) > 1 and item not in repeated:
        repeated += (item,)

print("Repeated items:", repeated)