# Read integers M and N
M = int(input())
N = int(input())

product = 0

# Loop from M to N and sum all odd numbers
# Note: Variable 'product' is used by the portal to store the sum.
for i in range(M, N + 1):
    if i % 2 != 0:
        product += i

print(product)
