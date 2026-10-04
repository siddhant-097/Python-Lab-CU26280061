# Unzip a list of tuples into individual lists

data = [(1, "A"), (2, "B"), (3, "C")]

numbers = []
letters = []

for item in data:
    numbers.append(item[0])
    letters.append(item[1])

print("Original list:", data)
print("First list:", numbers)
print("Second list:", letters)