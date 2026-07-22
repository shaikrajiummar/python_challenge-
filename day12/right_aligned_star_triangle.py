# Read the integer N
N = int(input())

# Loop from 1 to N to print a right-aligned star triangle
for i in range(1, N + 1):
    spaces = "  " * (N - i)
    stars = "* " * i
    print(spaces + stars)
