# Read the input word
word = input()

# Loop to print prefixes of the word in increasing length
for i in range(1, len(word) + 1):
    print(word[:i])
