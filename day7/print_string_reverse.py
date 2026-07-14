# Read the input string N
N = input()

length = len(N)

# Loop backwards through the indices and print characters in reverse
for i in range(length - 1, -1, -1):
    print(N[i])
