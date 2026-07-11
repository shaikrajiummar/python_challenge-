# Read integers M and N
M = int(input())
N = int(input())

# Loop from 1 to M for rows
for i in range(1, M + 1):
    # Print the row number 'i' repeated N times (separated by spaces)
    row = (str(i) + " ") * N
    print(row)
