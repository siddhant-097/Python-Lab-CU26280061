# Determine the type of a triangle using its sides

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

# Check triangle validity first.
if (side1 + side2 > side3 and
        side1 + side3 > side2 and
        side2 + side3 > side1):

    if side1 == side2 and side2 == side3:
        print("Equilateral triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("The given sides do not form a valid triangle.")