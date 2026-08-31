sentence = input()
words = sentence.split()

# Find the word that comes first alphabetically (case-insensitive)
first_word = min(words, key=str.lower)

print(first_word)