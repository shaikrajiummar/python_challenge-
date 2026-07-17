# Read the integer N
n = int(input())

# Loop from 1 to n to print the hollow left-aligned star triangle
for i in range(1, n + 1):
    if i == 1:
        print("*")
    elif i == n:
        print("* " * n)
    else:
        spaces = "  " * (i - 2)
        print("* " + spaces + "*")
