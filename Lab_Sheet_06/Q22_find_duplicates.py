# Find duplicate elements using sets

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate elements:", duplicates)