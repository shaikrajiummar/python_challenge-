# Read the input word
word = input()
n = len(word)

# Loop to print prefixes of the word in decreasing length
for i in range(n, 0, -1):
    print(word[:i])
