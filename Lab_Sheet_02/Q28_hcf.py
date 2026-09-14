# Find the HCF (Highest Common Factor) of two numbers using a loop

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Convert negative numbers to positive.
if number1 < 0:
    number1 = -number1

if number2 < 0:
    number2 = -number2

if number1 == 0 and number2 == 0:
    print("HCF is not defined for both numbers being zero.")
else:
    smaller = number1

    if number2 < smaller:
        smaller = number2

    hcf = 1

    # Check every number up to the smaller number.
    for number in range(1, smaller + 1):
        if number1 % number == 0 and number2 % number == 0:
            hcf = number

    print("HCF =", hcf)