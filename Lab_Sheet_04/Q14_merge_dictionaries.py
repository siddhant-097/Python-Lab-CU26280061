# Merge two dictionaries

dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

merged = {}

for key, value in dict1.items():
    merged[key] = value

for key, value in dict2.items():
    merged[key] = value

print("Merged dictionary:", merged)