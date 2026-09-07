# Calculate power using the exponentiation operator
base = float(input("Enter base: "))
exponent = int(input("Enter non-negative exponent: "))

if exponent >= 0:
    result = base ** exponent
    print("Result =", result)
else:
    print("Please enter a non-negative exponent.")

