# Read the integer N
N = int(input())

# Loop from 1 to N for rows
for i in range(1, N + 1):
    # Loop i times for columns and print row number 'i'
    for j in range(i):
        print(i, end=" ")
    print()
