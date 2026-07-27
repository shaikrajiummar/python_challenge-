# Read the size of the pyramid N
n = int(input())

# Loop to print the inverted star pyramid using string multiplication
for i in range(n):
    stars = 2 * (n - i) - 1
    space = 4 * i
    row = " " * space + "* " * stars
    print(row)
