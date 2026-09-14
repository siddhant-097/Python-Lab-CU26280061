# Display multiplication tables from 1 to 10

for number in range(1, 11):
    print("\nMultiplication Table of", number)

    for multiplier in range(1, 11):
        result = number * multiplier
        print(number, "x", multiplier, "=", result)