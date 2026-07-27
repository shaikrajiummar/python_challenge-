# Read the input string
input_str = input()

vowels = "AEIOUaeiou"
result = ""

# Loop to collect only non-vowel characters
for char in input_str:
    if char not in vowels:
        result += char

# Print the resulting string without vowels
print(result)
