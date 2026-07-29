# Read size N
n = int(input())

# Loop to print the square pattern of descending numbers
for i in range(n):
    for j in range(n, 0, -1):
        print(j, end=" ")
    print()
