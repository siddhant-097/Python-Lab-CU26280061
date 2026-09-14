# Display grade based on marks

marks = float(input("Enter marks (0-100): "))

if marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 75 and marks < 90:
    grade = "B"
elif marks >= 50 and marks < 75:
    grade = "C"
elif marks >= 0 and marks < 50:
    grade = "F"
else:
    grade = "Invalid marks"

print("Marks:", marks)
print("Grade:", grade)