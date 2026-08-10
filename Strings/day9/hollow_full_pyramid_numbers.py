# Read size N
n = int(input())

# Loop to print the hollow full pyramid of numbers
for i in range(1, n + 1):
    # Spaces before the numbers to align the pyramid
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        # Print number on the boundary (first col, last col, or bottom row)
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            # Print space for the hollow center
            print(" ", end=" ")

    print()
