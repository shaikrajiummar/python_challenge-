# Read size N
n = int(input())
current = 1

# Loop to print Floyd's Triangle of numbers
for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        row += str(current) + " "
        current += 1
    print(row)
