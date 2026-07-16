# Read the integer N
n = int(input())

# Print the top half of the butterfly pattern
for i in range(1, n + 1):
    stars = "* " * i
    spaces = "  " * (2 * (n - i))
    row = stars + spaces + stars
    print(row)

# Print the bottom half of the butterfly pattern
for i in range(1, n):
    stars = "* " * (n - i)
    spaces = "  " * (2 * i)
    row = stars + spaces + stars
    print(row)
