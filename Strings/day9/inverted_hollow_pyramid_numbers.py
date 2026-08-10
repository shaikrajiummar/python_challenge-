# Read size N and starting number S
n = int(input())
s = int(input())

# Loop to print the inverted hollow pyramid pattern of numbers
for i in range(n):
    # Print leading spaces for alignment (single spaces matching NxtWave pattern)
    print(" " * i, end="")

    for j in range(i, n):
        if i == 0:
            print(s + j, end=" ")
        elif j == i:
            print(s, end=" ")
        elif j == n - 1:
            print(s + n - i - 1, end=" ")
        else:
            print("  ", end="")

    print()
