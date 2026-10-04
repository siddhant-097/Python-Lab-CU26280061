# Convert a tuple into a string

my_tuple = ("Python", "is", "easy")

result = ""

for item in my_tuple:
    result += item + " "

result = result.strip()

print("Tuple:", my_tuple)
print("String:", result)