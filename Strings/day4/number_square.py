# Read size N
n = int(input())

# Loop to print the square pattern of numbers
for i in range(n):
    row = ""
    for j in range(1, n + 1):
        row += str(j) + " "
    print(row)
