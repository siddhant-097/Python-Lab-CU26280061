# Separate even and odd numbers from a list

input_values = input("Enter integers separated by spaces: ").split()

numbers = []
even_numbers = []
odd_numbers = []

for value in input_values:
    numbers.append(int(value))

# Separate even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Original list:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
