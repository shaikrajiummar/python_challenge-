# Read the size of the square N
N = int(input())

# Loop to print the square pattern of row indices
for i in range(N):
    for j in range(N):
        print(i, end=" ")
    print()
