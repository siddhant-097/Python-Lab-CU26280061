# Perform union, intersection, difference and symmetric difference

set1 = set(map(int, input("Enter elements of set1: ").split()))
set2 = set(map(int, input("Enter elements of set2: ").split()))

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric difference:", set1 ^ set2)