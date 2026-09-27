# Reverse a list without using reversed()

input_values = input("Enter elements separated by spaces: ").split()

print("Reversed list:", end=" ")

for index in range(len(input_values) - 1, -1, -1):
    print(input_values[index], end=" ")

print()
