# Find common letters in two strings

string1 = input("Enter first string: ").lower()
string2 = input("Enter second string: ").lower()

letters1 = set(string1)
letters2 = set(string2)

common = letters1.intersection(letters2)
common.discard(" ")

print("Common letters:", common)