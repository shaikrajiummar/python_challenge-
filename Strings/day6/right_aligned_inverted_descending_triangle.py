# Read size N
n = int(input())

# Calculate total count of numbers K using the arithmetic progression formula
k = (n * (n + 1)) // 2
current_number = k

# Loop to print the right-aligned inverted descending number triangle
for i in range(n):
    # Calculate spaces: 0 double spaces for row 0, 1 for row 1, etc.
    spaces = "  " * i
    
    # Calculate elements to print: starts at N and decreases by 1 per row
    row_elements = n - i
    
    row_output = spaces
    for j in range(row_elements):
        row_output += str(current_number) + " "
        current_number -= 1
        
    print(row_output)
