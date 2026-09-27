# Count the number of vowels and consonants in a string

text = input("Enter a string: ")

vowels = 0
consonants = 0

for character in text:
    if character.isalpha():
        if character.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
