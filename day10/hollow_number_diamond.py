# Read the integer N
n = int(input())

# Loop to print the top half of the hollow number diamond
for i in range(1, n + 1):
    if i == 1:
        row = str(i)
    else:
        spaces = " " * ((2 * i) - 3)
        row = str(i) + spaces + str(i)
    print(row)

# Loop to print the bottom half of the hollow number diamond
for i in range(1, n):
    num = n - i
    if num == 1:
        row = str(1)
    else:
        spaces = " " * (2 * num - 3)
        row = str(num) + spaces + str(num)
    print(row)
