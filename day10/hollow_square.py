# Read the integer N
n = int(input())

# Loop from 1 to n to print the hollow square pattern
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        spaces = "  " * (n - 2)
        print("* " + spaces + "*")
