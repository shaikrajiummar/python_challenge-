# Read size N
n = int(input())
current_number = 1

# Loop to print the sequential number square pattern
for i in range(n):
    row_output = ""
    for j in range(n):
        row_output += str(current_number) + " "
        current_number += 1
    print(row_output)
