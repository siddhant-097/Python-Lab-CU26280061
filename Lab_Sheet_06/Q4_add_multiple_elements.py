# Add multiple elements to a set

my_set = {10, 20, 30}

numbers = set(map(int, input("Enter numbers separated by spaces: ").split()))
my_set.update(numbers)

print("Updated set:", my_set)