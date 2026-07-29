# Read starting number S and size N
s = int(input())
n = int(input())

# Loop to print the right-aligned triangle of numbers starting from S
for i in range(1, n + 1):
    spaces = " " * (n - i)
    row = ""
    for j in range(s, s + i):
        row += str(j) + " "
    print(spaces + row)
