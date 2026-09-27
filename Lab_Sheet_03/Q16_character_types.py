# Count digits, alphabets, and special characters

text = input("Enter a string: ")

digits = 0
alphabets = 0
special_characters = 0

for character in text:
    if character.isdigit():
        digits += 1
    elif character.isalpha():
        alphabets += 1
    else:
        special_characters += 1

print("Number of alphabets:", alphabets)
print("Number of digits:", digits)
print("Number of special characters:", special_characters)
