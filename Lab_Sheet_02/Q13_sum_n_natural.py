# Find the sum of first n natural numbers

n = int(input("Enter the value of n: "))

sum_of_numbers = 0

for number in range(1, n + 1):
    sum_of_numbers += number

print("Sum of first", n, "natural numbers =", sum_of_numbers)