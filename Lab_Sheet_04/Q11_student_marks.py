# Create and display student marks dictionary

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("Student Details:")

for name, marks in students.items():
    print(name, ":", marks)