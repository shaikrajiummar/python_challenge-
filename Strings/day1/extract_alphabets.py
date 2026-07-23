# Read the input string
input_string = input()
result = ""

# Loop through characters and collect only alphabets
for char in input_string:
    if char.isalpha():
        result += char

print(result)
