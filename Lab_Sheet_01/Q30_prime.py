# Check whether a number is prime
num = int(input("Enter an integer: "))

if num < 2:
    print("Not a prime number")
else:
    is_prime = True

    # Check divisibility from 2 up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")