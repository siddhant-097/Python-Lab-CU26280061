# Sort the characters of a string alphabetically
# Bubble sort is used instead of sorted()

text = input("Enter a string: ")

characters = []

for character in text:
    characters.append(character)

# Bubble sort
for i in range(len(characters)):
    for j in range(0, len(characters) - i - 1):
        if characters[j].lower() > characters[j + 1].lower():
            temp = characters[j]
            characters[j] = characters[j + 1]
            characters[j + 1] = temp

result = ""

for character in characters:
    result += character

print("Characters in alphabetical order:", result)
