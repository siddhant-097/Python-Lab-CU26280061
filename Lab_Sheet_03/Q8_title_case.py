# Convert a string into title case without using title()

text = input("Enter a string: ")

result = ""
new_word = True

for character in text:
    if character == " ":
        result += character
        new_word = True
    else:
        if new_word:
            result += character.upper()
            new_word = False
        else:
            result += character.lower()

print("Title case:", result)
