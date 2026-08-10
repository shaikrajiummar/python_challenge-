# Read rows M and columns N on separate lines
m = int(input())
n = int(input())

# Loop to print the hollow rectangle of numbers starting from 7 per row
for i in range(m):
    for j in range(n):
        num = 7 + j
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            print(num, end=" ")
        else:
            # Print spaces matching the length of the number plus the trailing space
            print(" " * len(str(num)) + " ", end="")
    print()
