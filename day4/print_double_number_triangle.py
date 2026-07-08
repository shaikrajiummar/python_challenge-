# Read the integer N
N = int(input())

# Outer loop to repeat the pattern 2 times
for i in range(2):
    # Loop for rows from 1 to N
    for j in range(1, N + 1):
        # Loop for columns and print the row number 'j' repeated j times
        for k in range(j):
            print(j, end="")
        print()
