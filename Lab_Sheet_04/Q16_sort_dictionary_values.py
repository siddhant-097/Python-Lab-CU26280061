# Sort dictionary by values

data = {"Rahul": 85, "Aman": 92, "Priya": 78}

sorted_items = sorted(data.items(), key=lambda item: item[1])

sorted_dict = {}

for key, value in sorted_items:
    sorted_dict[key] = value

print("Dictionary sorted by values:", sorted_dict)