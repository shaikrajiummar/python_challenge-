# Read integers M and N
M = int(input())
N = int(input())

product = 1

# Loop from M to N and calculate the product of numbers divisible by 3
for i in range(M, N + 1):
    if i % 3 == 0:
        product *= i

print(product)
