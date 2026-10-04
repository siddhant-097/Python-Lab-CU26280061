# Create a nested tuple and access its elements

my_tuple = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)

print("Nested tuple:", my_tuple)

print("First inner tuple:", my_tuple[0])
print("Element at row 2, column 2:", my_tuple[1][1])
print("Element at row 3, column 1:", my_tuple[2][0])