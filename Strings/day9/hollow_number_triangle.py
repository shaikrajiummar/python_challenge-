# Read size N
n = int(input())

# Loop to print the hollow right-angled triangle pattern of numbers
for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Print numbers only on boundaries (first column, diagonal, or bottom row)
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
