# Read the integer N
n = int(input())

# Loop from 1 to n to print the dot and zero triangle pattern
for i in range(1, n + 1):
    if i == 1:
        print(".")
    elif i == 2:
        print(". .")
    elif i == n:
        print(". " * n)
    else:
        row = ". "
        row += "0 " * (i - 2)
        row += "."
        print(row)
