# Rotate a list to the left by n positions

numbers = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter number of positions: "))

if len(numbers) > 0:
    n = n % len(numbers)
    rotated = numbers[n:] + numbers[:n]
else:
    rotated = numbers

print("Rotated list:", rotated)
