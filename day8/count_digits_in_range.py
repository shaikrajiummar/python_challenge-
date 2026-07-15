# Read integers M and N
M = int(input())
N = int(input())

digits = 0

# Loop from M to N and accumulate the length (number of digits) of each number
for i in range(M, N + 1):
    length = len(str(i))
    digits += length

print(digits)
