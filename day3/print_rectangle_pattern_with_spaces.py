# Read height M and width N
M = int(input())
N = int(input())

# Outer loop for rows
for i in range(M):
    # Inner loop for columns
    for j in range(N):
        print("* ", end="")
    print()
