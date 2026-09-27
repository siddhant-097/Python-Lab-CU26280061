# Create dictionary of numbers and squares

n = int(input("Enter the value of n: "))

squares = {}

for num in range(1, n + 1):
    squares[num] = num * num

print("Squares dictionary:", squares)