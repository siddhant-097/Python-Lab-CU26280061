# Find maximum and minimum values in a set

numbers = set(map(int, input("Enter numbers separated by spaces: ").split()))

if numbers:
    print("Maximum value:", max(numbers))
    print("Minimum value:", min(numbers))
else:
    print("Set is empty.")
    