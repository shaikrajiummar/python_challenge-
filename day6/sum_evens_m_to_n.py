# Read integers M and N
M = int(input())
N = int(input())

sum = 0

# Loop from M to N and sum all even numbers
for i in range(M, N + 1):
    if i % 2 == 0:
        sum += i

# Print the final sum
print(sum)
