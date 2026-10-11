# Remove elements of set2 from set1

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5}

set1.difference_update(set2)

print("Updated set1:", set1)