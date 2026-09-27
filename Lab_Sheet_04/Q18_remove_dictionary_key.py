# Remove a key from dictionary

student = {"Name": "Rahul", "Age": 20, "Marks": 85}

key = input("Enter key to remove: ")

if key in student:
    del student[key]
    print("Updated dictionary:", student)
else:
    print("Key not found.")