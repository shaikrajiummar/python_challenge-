# Read integers M and N
M = int(input())
N = int(input())

product = 1

# Loop from M to N and calculate the cumulative product
for i in range(M, N + 1):
    product *= i

print(product)
