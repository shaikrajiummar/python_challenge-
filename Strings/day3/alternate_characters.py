# Read the two input strings
s1 = input()
s2 = input()
result = ""

# Loop to combine characters: even index from s1, odd index from s2
for i in range(len(s1)):
    if i % 2 == 0:
        result += s1[i]
    else:
        result += s2[i]

# Print the resulting string
print(result)
