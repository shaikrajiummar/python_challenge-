# Read height M and width N
M = int(input())
N = int(input())

# Loop M times and print a row of N stars
for i in range(1, M + 1):
    print("*" * N)
