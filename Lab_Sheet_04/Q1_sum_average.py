# Find sum and average of list elements

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

total = 0

for num in numbers:
    total += num

average = total / len(numbers) if len(numbers) > 0 else 0

print("Sum:", total)
print("Average:", average)