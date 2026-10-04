# Find common elements between two tuples

tuple1 = tuple(input("Enter first tuple elements: ").split())
tuple2 = tuple(input("Enter second tuple elements: ").split())

common = ()

for item in tuple1:
    if item in tuple2 and item not in common:
        common += (item,)

print("Common elements:", common)