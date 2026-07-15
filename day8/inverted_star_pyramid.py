# Read the integer N
N = int(input())

# Loop from 0 to N-1 and print an inverted star pyramid
for i in range(N):
    spaces = " " * i
    star = "*" * (2 * (N - i) - 1)
    print(spaces + star)
