# Read size N
n = int(input())

# Loop to print the double number triangle pattern
for m in range(1, n + 1):
    row_output = ""
    
    # 1. Print numbers from 1 up to m
    for i in range(1, m + 1):
        row_output += str(i) + " "
        
    # 2. Print numbers from 1 up to (m - 1)
    for j in range(1, m):
        row_output += str(j) + " "
        
    print(row_output)
