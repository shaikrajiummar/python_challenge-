# Read the integer N
n = int(input())

# Loop from 1 to n to print a centered inverted star pyramid
for i in range(1, n + 1):
    spaces = " " * (i - 1)
    star = "* " * (n - i + 1)
    print(spaces + star)
