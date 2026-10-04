# Remove duplicate elements from a tuple

my_tuple = tuple(input("Enter tuple elements: ").split())

result = ()

for item in my_tuple:
    if item not in result:
        result += (item,)

print("Original tuple:", my_tuple)
print("Tuple without duplicates:", result)