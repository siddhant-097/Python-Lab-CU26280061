# Find the first non-repeated character in a string

text = input("Enter a string: ")

found = False

for character in text:
    frequency = 0

    for current_character in text:
        if current_character == character:
            frequency += 1

    if frequency == 1:
        print("First non-repeated character:", character)
        found = True
        break

if not found:
    print("There is no non-repeated character.")
