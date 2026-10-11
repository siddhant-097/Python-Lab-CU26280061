# Check whether two strings are anagrams

string1 = input("Enter first string: ").lower().replace(" ", "")
string2 = input("Enter second string: ").lower().replace(" ", "")

if len(string1) == len(string2) and set(string1) == set(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")