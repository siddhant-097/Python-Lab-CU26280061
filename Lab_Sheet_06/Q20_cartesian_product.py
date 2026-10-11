# Find the Cartesian product of two sets

set1 = {1, 2, 3}
set2 = {"A", "B"}

result = set()

for x in set1:
    for y in set2:
        result.add((x, y))

print("Cartesian product:", result)