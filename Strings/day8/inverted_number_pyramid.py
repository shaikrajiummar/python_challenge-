# Read size N
n = int(input())

# Loop to print the inverted number pyramid
for i in range(n, 0, -1):
    # Print leading spaces
    print(" " * (n - i), end="")
    
    # Print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
