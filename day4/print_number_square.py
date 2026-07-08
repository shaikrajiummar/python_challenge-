# Read the integer N
N = int(input())

# Loop N times for rows
for i in range(1, N + 1):
    # Loop N times for columns and print the row number 'i'
    for j in range(N):
        print(i, end="")
    print()
