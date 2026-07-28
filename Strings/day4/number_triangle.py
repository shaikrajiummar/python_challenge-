# Read size N
n = int(input())

# Loop to print the right-angled triangle of numbers
for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        row += str(j) + " "
    print(row)
