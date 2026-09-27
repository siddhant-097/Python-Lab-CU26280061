# Count the number of words in a string

text = input("Enter a string: ")

word_count = 0
inside_word = False

for character in text:
    if character != " " and not inside_word:
        word_count += 1
        inside_word = True
    elif character == " ":
        inside_word = False

print("Number of words:", word_count)
