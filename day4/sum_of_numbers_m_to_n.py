# Read integers M and N
M = int(input())
N = int(input())

sum = 0

# Loop from M to N and calculate the sum
for i in range(M, N + 1):
    sum = sum + i

# Print the final sum
print(sum)
