# Check if a number is a palindrome

number = int(input("Enter a number: "))

original_number = number
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number = number // 10

if original_number == reverse_number:
    print(original_number, "is a palindrome.")
else:
    print(original_number, "is not a palindrome.")