# Check whether a number lies within a given range
num = float(input("Enter a number: "))
lower = float(input("Enter lower limit: "))
upper = float(input("Enter upper limit: "))

if lower <= num <= upper:
    print("Number is within the range.")
else:
    print("Number is outside the range.")