# Read the integer N
N = int(input())

# Loop to print a right-aligned triangle where the last row is hashes and others are stars
for i in range(1, N + 1):
    space = " " * (N - i)
    if i == N:
        sy = "#" * i
    else:
        sy = "*" * i
    print(space + sy)
