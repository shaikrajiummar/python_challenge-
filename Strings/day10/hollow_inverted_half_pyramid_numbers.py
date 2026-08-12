# Read size N
n = int(input())

# Loop to print the hollow inverted half pyramid pattern of numbers
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        # Print numbers only on boundaries (first column, diagonal, or top row)
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            # Print space for the hollow center
            print(" ", end=" ")
    print()
