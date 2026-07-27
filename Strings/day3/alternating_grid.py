# Read the row size M and column size N
m = int(input())
n = int(input())

# Loop to print the alternating row grid (+ and -)
for i in range(m):
    if i % 2 == 0:
        print("+ " * n)
    else:
        print("- " * n)
