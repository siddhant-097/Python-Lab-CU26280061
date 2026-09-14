# Find the absolute value of a number

number = float(input("Enter a number: "))

if number < 0:
    absolute_value = -number
else:
    absolute_value = number

print("Absolute value =", absolute_value)