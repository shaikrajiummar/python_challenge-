# Read the input string N
N = input()

# Define string of vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Loop through each character in N and print if it is a vowel
for char in N:
    if char in vowels:
        print(char)
