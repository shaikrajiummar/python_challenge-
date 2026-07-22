# Read the word input
word = input()

# Get the first character of the word
char = word[0]

# Print the character N times, where N is the length of the word
N = len(word)
for i in range(N):
    print(char)
