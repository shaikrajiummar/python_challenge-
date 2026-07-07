# Read the input string
a = input()
len_of_a = len(a)

# Start string b with the first character
b = a[0]

# Loop through the rest of the characters and add a hyphen between them
for i in range(1, len_of_a):
    b = b + "-" + a[i]

print(b)
