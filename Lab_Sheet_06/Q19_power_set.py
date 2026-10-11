# Create the power set of a given set

from itertools import combinations

my_set = set(map(int, input("Enter distinct numbers: ").split()))
elements = list(my_set)

power_set = []

for size in range(len(elements) + 1):
    for group in combinations(elements, size):
        power_set.append(set(group))

print("Power set:")
for subset in power_set:
    print(subset)