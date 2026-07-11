# Read integers M and N
M = int(input())
N = int(input())

# Loop M times for rows and print N pluses (separated by spaces)
for i in range(M):
    row = "+ " * N
    print(row)
