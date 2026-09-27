# Create a nested dictionary for student details

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    students[roll] = {
        "Name": name,
        "Roll": roll,
        "Marks": marks
    }

print("Student Details:")

for roll, details in students.items():
    print(roll, ":", details)