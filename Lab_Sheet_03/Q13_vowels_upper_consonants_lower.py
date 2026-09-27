# Convert vowels to uppercase and consonants to lowercase

text = input("Enter a string: ")

result = ""

for character in text:
    if character.isalpha():
        if character.lower() in "aeiou":
            result += character.upper()
        else:
            result += character.lower()
    else:
        result += character

print("Result:", result)
