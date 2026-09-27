# Replace all spaces in a string with underscores

text = input("Enter a string: ")

result = ""

for character in text:
    if character == " ":
        result += "_"
    else:
        result += character

print("String after replacement:", result)
