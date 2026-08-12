# Read size N
n = int(input())

# Loop to print the hollow pyramid pattern of numbers starting from 5
for i in range(1, n + 1):
    # Spaces before the numbers
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        # Print numbers on boundaries based on columns and row position
        if j == 1:
            print(5, end=" ")
        elif j == i:
            print(5 + i - 1, end=" ")
        elif i == n:
            print(5 + j - 1, end=" ")
        else:
            print(" ", end=" ")

    print()
