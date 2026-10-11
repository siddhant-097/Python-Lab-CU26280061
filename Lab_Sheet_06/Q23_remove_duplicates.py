# Remove duplicates from a list using a set

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = list(set(numbers))

print("List without duplicates:", unique_numbers)