# Check whether a character is a vowel or consonant
ch = input("Enter a single alphabet character: ")

if len(ch) == 1 and ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Please enter a single alphabet character.")