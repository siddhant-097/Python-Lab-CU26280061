# Create a list of squares from 1 to n

n = int(input("Enter the value of n: "))

squares = []

for num in range(1, n + 1):
    squares.append(num * num)

print("List of squares:", squares)