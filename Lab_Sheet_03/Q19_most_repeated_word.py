# Find the most repeated word in a string

text = input("Enter a sentence: ")

words = text.lower().split()

if len(words) == 0:
    print("No words were entered.")
else:
    most_repeated_word = words[0]
    highest_frequency = 0

    for word in words:
        frequency = 0

        for current_word in words:
            if current_word == word:
                frequency += 1

        if frequency > highest_frequency:
            highest_frequency = frequency
            most_repeated_word = word

    print("Most repeated word:", most_repeated_word)
    print("Frequency:", highest_frequency)
