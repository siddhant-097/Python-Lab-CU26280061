# Find common elements in two lists

list1 = input("Enter elements of first list: ").split()
list2 = input("Enter elements of second list: ").split()

common_elements = []

for element in list1:
    if element in list2 and element not in common_elements:
        common_elements.append(element)

if len(common_elements) == 0:
    print("There are no common elements.")
else:
    print("Common elements:", common_elements)
