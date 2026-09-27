# Remove all punctuation from a string

text = input("Enter a string: ")

punctuation = ".,!?;:'\"-()[]{}<>/\\@#$%^&*_+=|`~"
result = ""

for character in text:
    if character not in punctuation:
        result += character

print("String without punctuation:", result)
