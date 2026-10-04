# Find the length of the longest word

words = tuple(input("Enter words separated by spaces: ").split())

if words:
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("Tuple is empty.")