# Find remainder using the modulo operator
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

if b != 0:
    remainder = a % b
    print("Remainder =", remainder)
else:
    print("Division by zero is not allowed.")