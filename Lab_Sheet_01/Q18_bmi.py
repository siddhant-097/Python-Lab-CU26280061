# Calculate Body Mass Index
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

if height > 0:
    bmi = weight / (height ** 2)
    print("BMI =", round(bmi, 2))
else:
    print("Height must be greater than zero.")