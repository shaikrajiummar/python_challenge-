# Read the size N
N = int(input())

# Loop to print the hollow square pattern using grid characters (+ - |)
for i in range(N + 2):
    if i == 0 or i == N + 1:
        print("+", end=" ")
        for j in range(N):
            print("-", end=" ")
        print("+")
    else:
        print("|", end=" ")
        for j in range(N):
            print(" ", end=" ")
        print("|")
