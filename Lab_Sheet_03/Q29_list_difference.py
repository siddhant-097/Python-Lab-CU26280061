# Find elements that are present in the first list
# but not present in the second list.

list1 = input("Enter elements of first list: ").split()
list2 = input("Enter elements of second list: ").split()

difference = []

for element in list1:
    if element not in list2 and element not in difference:
        difference.append(element)

print("Elements present in first list but not second:", difference)
