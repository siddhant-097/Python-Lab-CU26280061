# Check whether two strings are anagrams

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

string1 = string1.lower()
string2 = string2.lower()

# Remove spaces manually
clean_string1 = ""
clean_string2 = ""

for character in string1:
    if character != " ":
        clean_string1 += character

for character in string2:
    if character != " ":
        clean_string2 += character

if len(clean_string1) != len(clean_string2):
    print("The strings are not anagrams.")
else:
    is_anagram = True
    checked = ""

    for character in clean_string1:
        if character not in checked:
            count1 = 0
            count2 = 0

            for current in clean_string1:
                if current == character:
                    count1 += 1

            for current in clean_string2:
                if current == character:
                    count2 += 1

            if count1 != count2:
                is_anagram = False
                break

            checked += character

    if is_anagram:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
