# Read N (rows) and S (starting number)
n = int(input())
s = int(input())

# Loop to print the inverted hollow pyramid pattern of numbers
for r in range(n):
    # Print leading spaces for alignment
    print(" " * r, end="")
    
    row_elements = n - r
    for j in range(row_elements):
        num = s + j
        # Print numbers on boundaries: top row, first column, or last column
        if r == 0 or j == 0 or j == row_elements - 1:
            print(num, end=" ")
        else:
            # Print spaces matching the size of the number plus the trailing space
            print(" " * len(str(num)) + " ", end="")
    print()
