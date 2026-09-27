# Update a dictionary value

student = {"Name": "Rahul", "Age": 20, "Marks": 85}

key = input("Enter key to update: ")

if key in student:
    new_value = input("Enter new value: ")
    student[key] = new_value
    print("Dictionary updated:", student)
else:
    print("Key does not exist.")