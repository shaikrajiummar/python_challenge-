# Read size N
n = int(input())

# Loop to print the pyramid pattern of numbers
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")
    
    # Print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()
