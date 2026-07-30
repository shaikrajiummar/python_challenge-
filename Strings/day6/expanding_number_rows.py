# Read starting number S and size N
s = int(input())
n = int(input())

current_number = s
# The number of elements in the row increases sequentially (2, 4, 6...)
row_elements = 2

# Loop to print the expanding rows pattern of numbers
for i in range(n):
    row_output = ""
    for j in range(row_elements):
        row_output += str(current_number) + " "
        current_number += 1
    print(row_output)
    row_elements += 2
