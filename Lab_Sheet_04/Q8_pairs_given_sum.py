# Find pairs whose sum equals the target

numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

print("Pairs with the required sum:")

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], "and", numbers[j])
            found = True

if not found:
    print("No pairs found.")
