# Read input string N
N = input()

vowels = 'aeiouAEIOU'
count = 0

# Loop through and count all vowels in N
for char in N:
    if char in vowels:
        count += 1

# Check if vowel count is strictly greater than 2
if count > 2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")
