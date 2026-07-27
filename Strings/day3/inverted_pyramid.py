# Read the size of the pyramid N
n = int(input())

# Loop to print the inverted star pyramid with increasing indentation
for i in range(n):
    print(" " * (4 * i), end="")
    for j in range(2 * (n - i) - 1):
        if j == 2 * (n - i) - 2:
            print("*", end="")
        else:
            print("* ", end="")
    print()
