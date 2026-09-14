# Print a pyramid pattern of numbers

rows = int(input("Enter the number of rows: "))

for row in range(1, rows + 1):

    # Print spaces before the numbers.
    for space in range(rows - row):
        print(" ", end="")

    # Print increasing numbers.
    for number in range(1, row + 1):
        print(number, end="")

    # Print decreasing numbers.
    for number in range(row - 1, 0, -1):
        print(number, end="")

    print()