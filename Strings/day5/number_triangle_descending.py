# Read size N
n = int(input())

# Loop to print the right-aligned descending number triangle
for i in range(1, n + 1):
    # Print leading spaces
    print("  " * (n - i), end="")

    # Print numbers from i down to 1
    for j in range(i, 0, -1):
        print(j, end=" ")

    print()
