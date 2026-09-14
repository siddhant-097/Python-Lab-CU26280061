# Find the LCM (Least Common Multiple) of two numbers using a loop

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Convert negative numbers to positive.
if number1 < 0:
    number1 = -number1

if number2 < 0:
    number2 = -number2

if number1 == 0 or number2 == 0:
    print("LCM =", 0)
else:
    if number1 > number2:
        lcm = number1
    else:
        lcm = number2

    # Continue until a common multiple is found.
    while lcm % number1 != 0 or lcm % number2 != 0:
        lcm += 1

    print("LCM =", lcm)