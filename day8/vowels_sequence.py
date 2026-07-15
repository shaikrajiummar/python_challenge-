# Read the input string N
N = input()

vowels = "aeiouAEIOU"
res = ""

# Loop through N and construct a string of vowels only
for char in N:
    if char in vowels:
        res += char

print(res)
