# Sort dictionary by keys

data = {"c": 30, "a": 10, "b": 20}

sorted_dict = {}

for key in sorted(data):
    sorted_dict[key] = data[key]

print("Dictionary sorted by keys:", sorted_dict)