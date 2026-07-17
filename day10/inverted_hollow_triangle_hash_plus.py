# Read the integer N
n = int(input())

# Loop from 1 to n to print the inverted hollow right-angled triangle
for i in range(1, n + 1):
    if i == 1:
        row = ("# " * (n - 1)) + "#"
    elif i == n:
        row = "+"
    else:
        middle = 2 * (n - i) - 1
        spaces = " " * middle
        row = "+" + spaces + "+"
    print(row)
