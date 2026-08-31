n = int(input())

for i in range(1, n + 1):
    # Print leading spaces (2 spaces per missing character)
    spaces = "  " * (n - i)
    
    # Build the characters string starting from 'A' up to the i-th character
    row_str = ""
    for j in range(i):
        row_str += chr(65 + j) + " "
        
    print(spaces + row_str)