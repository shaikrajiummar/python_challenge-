# Read the size of the square N
N = int(input())

# Construct the number row
row = " "
for i in range(1, N + 1):
    row = row + str(i) + " "

# Print the constructed row N times
for i in range(N):
    print(row)
