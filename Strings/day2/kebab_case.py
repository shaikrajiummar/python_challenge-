# Read the input string
s = input()
result = ""

# Loop to convert camelCase/PascalCase to kebab-case
for i in range(len(s)):
    if s[i].isupper():
        if i == 0:
            result += s[i].lower()
        else:
            result += "-" + s[i].lower()
    else:
        result += s[i]

# Print the kebab-case string
print(result)
