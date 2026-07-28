# Read starting number S and size N
s = int(input())
n = int(input())

# Loop to print slanted column of numbers
for i in range(1, n + 1):
    spaces = " " * (n - i)
    row = ""
    for j in range(s, s + 1):
        row += str(j) + " "
    print(spaces + row)
