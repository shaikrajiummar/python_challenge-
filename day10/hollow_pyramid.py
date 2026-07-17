# Read the integer N
n = int(input())

# Loop from 1 to n to print a centered hollow pyramid
for i in range(1, n + 1):
    if i == 1:
        row = " " * (n - i) + "*"
    elif i == n:
        row = "* " * n
    else:
        left = " " * (n - i)
        holl = " " * (2 * (i - 2))
        row = left + "* " + holl + "* "
    print(row)
