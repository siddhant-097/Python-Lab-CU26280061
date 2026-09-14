# Check if a number is a Strong number
# A Strong number is a number whose sum of factorials
# of its digits is equal to the original number.

number = int(input("Enter a non-negative integer: "))

original_number = number
sum_of_factorials = 0

while number > 0:
    digit = number % 10

    # Find factorial of the current digit.
    factorial = 1

    for i in range(1, digit + 1):
        factorial *= i

    sum_of_factorials += factorial
    number = number // 10

# Special case for 0: 0! = 1.
if original_number == 0:
    sum_of_factorials = 1

if sum_of_factorials == original_number:
    print(original_number, "is a Strong number.")
else:
    print(original_number, "is not a Strong number.")