# Read the input string s
s = input()
result = ""

# Loop len(s) times to read indices and construct the result string
for i in range(len(s)):
    index = int(input())
    result += s[index]

# Print the final reconstructed string
print(result)
