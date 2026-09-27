# Find the largest and smallest elements in a list

numbers = input("Enter numbers separated by spaces: ").split()

if len(numbers) == 0:
    print("No numbers were entered.")
else:
    numbers_list = []

    for number in numbers:
        numbers_list.append(int(number))

    smallest = numbers_list[0]
    largest = numbers_list[0]

    for number in numbers_list:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

    print("List:", numbers_list)
    print("Smallest element:", smallest)
    print("Largest element:", largest)
