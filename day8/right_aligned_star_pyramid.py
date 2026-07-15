# Read the integer N
N = int(input())

# Loop from 1 to N and print a right-aligned star pyramid
for i in range(1, N + 1):
    spaces = "  " * (N - i)
    star = "* " * ((2 * i) - 1)
    print(spaces + star)
