# Remove duplicate values from dictionary

data = {"a": 10, "b": 20, "c": 10, "d": 30}

result = {}

for key, value in data.items():
    if value not in result.values():
        result[key] = value

print("Original dictionary:", data)
print("After removing duplicate values:", result)