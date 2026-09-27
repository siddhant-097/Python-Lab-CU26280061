# Remove duplicate elements from a list without using set()

input_values = input("Enter elements separated by spaces: ").split()

unique_elements = []

for value in input_values:
    if value not in unique_elements:
        unique_elements.append(value)

print("Original list:", input_values)
print("List after removing duplicates:", unique_elements)
