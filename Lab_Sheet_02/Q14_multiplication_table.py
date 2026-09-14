# Print the multiplication table of a given number

number = int(input("Enter a number: "))

print("Multiplication Table of", number)

for multiplier in range(1, 11):
    result = number * multiplier
    print(number, "x", multiplier, "=", result)