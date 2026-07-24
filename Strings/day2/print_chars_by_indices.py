# Read the input string s
s = input()

# Loop len(s) times to read indices and print characters at those indices
for i in range(len(s)):
    index = int(input())
    print(s[index])
