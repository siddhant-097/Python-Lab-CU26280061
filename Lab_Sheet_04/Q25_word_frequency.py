# Count word frequency in a paragraph

paragraph = input("Enter a paragraph: ").lower()

words = paragraph.split()
frequency = {}

for word in words:
    word = word.strip(".,!?;:")

    if word:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

print("Word frequency:", frequency)