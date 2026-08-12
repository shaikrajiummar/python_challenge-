# Read size N
n = int(input())

# Loop to print the hollow right-aligned descending number triangle
for i in range(1, n + 1):
    # Print leading double spaces
    print("  " * (n - i), end="")

    # Loop from i down to 1
    for j in range(i, 0, -1):
        # Print numbers only on boundaries (bottom row, first column of row, or last column of row)
        if i == n or j == i or j == 1:
            print(j, end=" ")
        else:
            # Print double spaces for the hollow interior
            print("  ", end="")

    print()
