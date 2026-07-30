# Read M (rows) and N (columns)
m = int(input())
n = int(input())

# Start from total count of numbers (M * N)
current_number = m * n

# Loop to print the descending number grid pattern
for i in range(m):
    row_output = ""
    for j in range(n):
        row_output += str(current_number) + " "
        current_number -= 1
    print(row_output)
