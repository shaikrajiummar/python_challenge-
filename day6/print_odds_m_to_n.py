# Read integers M and N
M = int(input())
N = int(input())

# Loop from M to N and print all odd numbers on the same line
for i in range(M, N + 1):
    if i % 2 != 0:
        print(i, end=" ")
