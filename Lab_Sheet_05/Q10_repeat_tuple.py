# Repeat a tuple n times

my_tuple = tuple(input("Enter tuple elements: ").split())

n = int(input("Enter number of repetitions: "))

result = my_tuple * n

print("Repeated tuple:", result)