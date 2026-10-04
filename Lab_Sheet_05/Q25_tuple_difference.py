# Find elements present in the first tuple but not in the second

tuple1 = tuple(input("Enter first tuple elements: ").split())
tuple2 = tuple(input("Enter second tuple elements: ").split())

difference = ()

for item in tuple1:
    if item not in tuple2 and item not in difference:
        difference += (item,)

print("Difference:", difference)