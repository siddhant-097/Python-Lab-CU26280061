# Find the smallest among three numbers

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

if number1 <= number2 and number1 <= number3:
    smallest = number1
elif number2 <= number1 and number2 <= number3:
    smallest = number2
else:
    smallest = number3

print("Smallest number =", smallest)