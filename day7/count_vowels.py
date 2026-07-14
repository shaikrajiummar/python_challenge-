# Read the input string N
N = input()

count = 0
vowels = 'aeiouAEIOU'

# Loop through each character in N and count if it is a vowel
for char in N:
    if char in vowels:
        count += 1

print(count)
