# Read integers M and N
M = int(input())
N = int(input())

count = 1

# Print the next N consecutive numbers starting from M + 1
while count <= N:
    print(M + count)
    count += 1
