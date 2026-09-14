# Check if a number is a multiple of both 3 and 7.

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 7 == 0:
    print(f"{number} is a multiple of both 3 and 7.")
else:
    print(f"{number} is not a multiple of both 3 and 7.")