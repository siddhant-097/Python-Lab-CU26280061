# Reverse a number using a while loop

number = int(input("Enter a number: "))

original_number = number
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number = number // 10

print("Original number:", original_number)
print("Reversed number:", reverse_number)