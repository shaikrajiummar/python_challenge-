# Read the integer N
n = int(input())

# Loop backwards from n to 1 to print a hollow inverted pyramid
for i in range(n, 0, -1):
    if i == n:
        print("* " * n)
    elif i == 1:
        print(" " * (n - 1) + "*")
    else:
        leading_spaces = " " * (n - i)
        inner_spaces = " " * (2 * i - 3)
        print(leading_spaces + "*" + inner_spaces + "*")
