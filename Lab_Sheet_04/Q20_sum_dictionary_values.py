# Find sum of dictionary values

data = {"a": 10, "b": 20, "c": 30}

total = 0

for value in data.values():
    total += value

print("Sum of values:", total)