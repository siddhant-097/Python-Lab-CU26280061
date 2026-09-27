# Find the longest word in a string

text = input("Enter a string: ")

words = text.split()

if len(words) == 0:
    print("No words were entered.")
else:
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    print("Longest word:", longest_word)
    print("Length:", len(longest_word))
