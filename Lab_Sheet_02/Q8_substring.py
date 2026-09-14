# Check if a string contains a particular substring

text = input("Enter a string: ")
substring = input("Enter the substring to search for: ")

if substring in text:
    print("The string contains the given substring.")
else:
    print("The string does not contain the given substring.")