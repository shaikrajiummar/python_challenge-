# Read integers M and N
M = int(input())
N = int(input())

product = 0

# Loop backwards from N to M and print all odd numbers on the same line
# Note: Variable 'product' is defined but unused.
for i in range(N, M - 1, -1):
    if i % 2 != 0:
        print(i, end=" ")
