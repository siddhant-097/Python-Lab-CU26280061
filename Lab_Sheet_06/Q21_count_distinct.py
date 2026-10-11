# Count distinct elements in a list

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

distinct = set(numbers)

print("Distinct elements:", distinct)
print("Number of distinct elements:", len(distinct))