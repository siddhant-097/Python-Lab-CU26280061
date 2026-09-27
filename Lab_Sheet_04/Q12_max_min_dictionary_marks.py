# Find maximum and minimum marks

students = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Riya": 88
}

if students:
    maximum = max(students.values())
    minimum = min(students.values())

    print("Maximum marks:", maximum)
    print("Minimum marks:", minimum)
else:
    print("Dictionary is empty.")