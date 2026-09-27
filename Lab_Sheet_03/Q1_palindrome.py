# Check whether a string is a palindrome

text = input("Enter a string: ")

reverse_text = ""

# Reverse the string using a loop
for character in text:
    reverse_text = character + reverse_text

if text == reverse_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


