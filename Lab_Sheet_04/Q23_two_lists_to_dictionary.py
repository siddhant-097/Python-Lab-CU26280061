# Convert two lists into a dictionary

keys = input("Enter keys separated by spaces: ").split()
values = input("Enter values separated by spaces: ").split()

if len(keys) == len(values):
    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    print("Created dictionary:", result)
else:
    print("Both lists must have the same number of elements.")