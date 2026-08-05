# Read size N
n = int(input())

# Upper half of the number diamond (including the middle row)
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Lower half of the number diamond
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
