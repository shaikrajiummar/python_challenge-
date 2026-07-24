# Read starting number S and size N
S = int(input())
N = int(input())

# Loop to print the square pattern of numbers starting from S
for i in range(N):
    for j in range(S, S + N):
        print(j, end=" ")
    print()
