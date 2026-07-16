# Read the integer N
n = int(input())

# Loop from 1 to n to print a centered star pyramid
for i in range(1, n + 1):
    spaces = " " * (n - i)
    star = "* " * i
    print(spaces + star)
