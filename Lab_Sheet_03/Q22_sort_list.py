# Sort a list in ascending and descending order
# Bubble sort is used instead of sort()

input_values = input("Enter integers separated by spaces: ").split()

numbers = []

for value in input_values:
    numbers.append(int(value))

# Ascending order
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Ascending order:", numbers)

print("Descending order:", end=" ")

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=" ")
print()
