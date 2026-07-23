# Read the input string
input_string = input()
result = ""

# Loop through characters and collect only uppercase letters
for char in input_string:
    if char.isupper():
        result += char

print(result)
