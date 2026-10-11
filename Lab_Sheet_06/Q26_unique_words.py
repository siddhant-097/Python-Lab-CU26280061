# Find unique words in a sentence

sentence = input("Enter a sentence: ").lower()

words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))