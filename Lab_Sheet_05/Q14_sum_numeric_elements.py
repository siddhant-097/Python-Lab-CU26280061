# Calculate sum of numeric elements

my_tuple = (10, 20.5, "Python", 30, 15.5)

total = 0

for item in my_tuple:
    if isinstance(item, (int, float)):
        total += item

print("Tuple:", my_tuple)
print("Sum of numeric elements:", total)