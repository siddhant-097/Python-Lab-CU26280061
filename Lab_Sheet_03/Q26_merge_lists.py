# Merge two lists into one

values1 = input("Enter elements of first list: ").split()
values2 = input("Enter elements of second list: ").split()

merged_list = []

for element in values1:
    merged_list.append(element)

for element in values2:
    merged_list.append(element)

print("First list:", values1)
print("Second list:", values2)
print("Merged list:", merged_list)
