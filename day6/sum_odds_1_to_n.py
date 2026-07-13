# Read the integer N
N = int(input())

product = 0

# Loop from 1 to N and sum all odd numbers
# Note: Variable 'product' is used by the portal to store the sum.
for i in range(1, N + 1):
    if i % 2 != 0:
        product += i

print(product)
