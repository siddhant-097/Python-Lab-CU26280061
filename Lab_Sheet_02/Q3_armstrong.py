# Check if a number is an Armstrong number

number = int(input("Enter a number: "))

original_number = number
temp = number
number_of_digits = 0

# Count the number of digits
while temp > 0:
    number_of_digits += 1
    temp = temp // 10

# Find the sum of digits raised to the number of digits
temp = number
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** number_of_digits
    temp = temp // 10

if sum_of_powers == original_number:
    print(original_number, "is an Armstrong number.")
else:
    print(original_number, "is not an Armstrong number.")