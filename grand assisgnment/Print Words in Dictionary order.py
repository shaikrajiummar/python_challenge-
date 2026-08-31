sentence = input()
words = sentence.split()

# Sort words ignoring case sensitivity
sorted_words = sorted(words, key=str.lower)

first_word = sorted_words[0]
last_word = sorted_words[-1]

print(f"{first_word} {last_word}")