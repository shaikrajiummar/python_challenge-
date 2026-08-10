# Read size N
n = int(input())

# Loop to print the hollow pyramid pattern of numbers starting from 5
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        # Print numbers only on boundaries (first column, diagonal, or bottom row)
        if j == 1 or j == i or i == n:
            print(4 + j, end=" ")
        else:
            # Print space for the hollow center
            print(" ", end=" ")

    print()
