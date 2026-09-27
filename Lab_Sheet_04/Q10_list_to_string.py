# Convert a list into a string without join()

items = input("Enter words separated by spaces: ").split()

result = ""

for item in items:
    result += item + " "

result = result.rstrip()

print("Converted string:", result)