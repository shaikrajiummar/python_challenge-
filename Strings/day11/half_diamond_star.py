# Read size N
n = int(input())

# Upper half (including the middle row)
for i in range(1, n + 1):
    print("* " * i)

# Lower half
for i in range(n - 1, 0, -1):
    print("* " * i)
