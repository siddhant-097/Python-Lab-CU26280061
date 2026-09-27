# Check whether two strings are rotations of each other

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if len(string1) != len(string2):
    print("The strings are not rotations of each other.")
else:
    combined_string = string1 + string1

    if string2 in combined_string:
        print("The strings are rotations of each other.")
    else:
        print("The strings are not rotations of each other.")
