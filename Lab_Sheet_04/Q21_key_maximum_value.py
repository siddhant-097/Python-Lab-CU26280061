# Find key having maximum value

data = {"Rahul": 85, "Aman": 92, "Priya": 78}

if data:
    max_key = max(data, key=data.get)
    print("Key with maximum value:", max_key)
    print("Maximum value:", data[max_key])
else:
    print("Dictionary is empty.")