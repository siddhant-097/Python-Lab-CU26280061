# Check whether a key exists in a dictionary.
data = {"name": "Aman", "course": "MCA", "semester": 1}
key = input("Enter key to search: ")
if key in data: print("Key exists. Value:", data[key])
else: print("Key does not exist.")
