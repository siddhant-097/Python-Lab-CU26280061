# Count the number of digits in a number

number = int(input("Enter a number: "))

# Convert negative number to positive for counting digits.
if number < 0:
    number = -number

if number == 0:
    digit_count = 1
else:
    digit_count = 0

    while number > 0:
        digit_count += 1
        number = number // 10

print("Number of digits =", digit_count)