# Calculate percentage of five subjects
total_marks = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks in subject {i}: "))
    total_marks += marks

percentage = (total_marks / 500) * 100

print("Total Marks =", total_marks)
print("Percentage =", percentage, "%")