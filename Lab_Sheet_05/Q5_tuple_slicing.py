# Access tuple elements using slicing

my_tuple = tuple(input("Enter tuple elements: ").split())

start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

print("Sliced tuple:", my_tuple[start:end])