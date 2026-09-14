# Print a reverse right-angled star pattern

for row in range(5, 0, -1):
    for column in range(row):
        print("*", end=" ")

    print()