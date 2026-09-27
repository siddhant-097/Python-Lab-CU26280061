# Find the second largest number in a list

input_values = input("Enter numbers separated by spaces: ").split()

numbers = []

for value in input_values:
    numbers.append(int(value))

if len(numbers) < 2:
    print("At least two numbers are required.")
else:
    # Remove duplicate values manually
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    if len(unique_numbers) < 2:
        print("A second largest number does not exist.")
    else:
        # Sort the list in ascending order using bubble sort
        for i in range(len(unique_numbers)):
            for j in range(0, len(unique_numbers) - i - 1):
                if unique_numbers[j] > unique_numbers[j + 1]:
                    temp = unique_numbers[j]
                    unique_numbers[j] = unique_numbers[j + 1]
                    unique_numbers[j + 1] = temp

        print("Second largest number:", unique_numbers[-2])
