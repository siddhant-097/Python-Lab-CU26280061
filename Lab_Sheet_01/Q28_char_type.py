# Check the type of a character
ch = input("Enter a single character: ")

if len(ch) == 1:
    if ch.isupper():
        print("Uppercase character")
    elif ch.islower():
        print("Lowercase character")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special character")
else:
    print("Please enter exactly one character.")