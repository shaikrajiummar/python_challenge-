# Read grid dimensions M (rows) and N (columns)
m = int(input())
n = int(input())

current = 1

# Loop to print sequential numbers in an M x N grid
for i in range(m):
    row = ""
    for j in range(n):
        row += str(current) + " "
        current += 1
    print(row)
