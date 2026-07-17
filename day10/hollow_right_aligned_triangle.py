# Read the integer N
n = int(input())

# Loop from 1 to N and print a right-aligned hollow triangle
for i in range(1, n + 1):
    if i == 1:
        left = " " * 2 * (n - 1)
        row = left + "*"
    elif i == n:
        row = "* " * n
    else:
        left = " " * 2 * (n - i)
        middle = " " * (2 * (i - 1) - 1)
        row = left + "*" + middle + "*"
    print(row)
