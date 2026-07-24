# Read the size N
N = int(input())

# Loop to print the left-aligned odd star triangle using nested loops
for i in range(1, N + 1):
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
