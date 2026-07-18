# Read the integer N
N = int(input())

# Loop to print the top half of the hollow butterfly pattern
for i in range(1, N + 1):
    left = "*"
    if i > 1:
        left = "*" + " " * (2 * i - 3) + "*"
    middle = " " * (4 * (N - i) + 1)
    print(left + middle + left)

# Loop to print the bottom half of the hollow butterfly pattern
for i in range(N, 0, -1):
    left = "*"
    if i > 1:
        left = "*" + " " * (2 * i - 3) + "*"
    middle = " " * (4 * (N - i) + 1)
    print(left + middle + left)
