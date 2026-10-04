# Sort a tuple of strings alphabetically

words = tuple(input("Enter words separated by spaces: ").split())

sorted_tuple = tuple(sorted(words))

print("Original tuple:", words)
print("Sorted tuple:", sorted_tuple)