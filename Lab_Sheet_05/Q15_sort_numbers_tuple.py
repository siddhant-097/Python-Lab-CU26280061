# Sort a tuple of numbers

numbers = tuple(map(int, input("Enter numbers: ").split()))

sorted_tuple = tuple(sorted(numbers))

print("Original tuple:", numbers)
print("Sorted tuple:", sorted_tuple)