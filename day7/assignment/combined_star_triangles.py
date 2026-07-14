# Read the integer N
N = int(input())

# Print a right-angled star triangle of height N
for i in range(1, N + 1):
    print("* " * i)

# Print an inverted right-angled star triangle of height N
for i in range(N, 0, -1):
    print("* " * i)
