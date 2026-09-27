# Reverse a string without using slicing

text = input("Enter a string: ")

reverse_text = ""

for character in text:
    reverse_text = character + reverse_text

print("Reversed string:", reverse_text)
