# Read the input word
word = input()

# Convert the word to lowercase for case-insensitive comparison
lowercase = word.lower()

# Reverse the lowercase word
reverse = lowercase[::-1]

# Check if the word is a palindrome
if lowercase == reverse:
    print(True)
else:
    print(False)
