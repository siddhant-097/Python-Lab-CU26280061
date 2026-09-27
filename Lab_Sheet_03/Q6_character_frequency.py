# Find the frequency of each character in a string

text = input("Enter a string: ")

processed_characters = ""

for character in text:
    if character not in processed_characters:
        frequency = 0

        for current_character in text:
            if current_character == character:
                frequency += 1

        print("'" + character + "':", frequency)
        processed_characters += character
