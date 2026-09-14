# Check whether a number is a perfect number

number = int(input("Enter a positive integer: "))

sum_of_divisors = 0

# Find all proper divisors of the number.
for divisor in range(1, number):
    if number % divisor == 0:
        sum_of_divisors += divisor

if number > 0 and sum_of_divisors == number:
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")