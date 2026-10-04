# Find maximum and minimum values

numbers = tuple(map(int, input("Enter numbers: ").split()))

if numbers:
    print("Maximum value:", max(numbers))
    print("Minimum value:", min(numbers))
else:
    print("Tuple is empty.")