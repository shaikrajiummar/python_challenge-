# Read the integer N
N = int(input())

count = 1

# Loop N times and print the row number 'count' repeated N times
while count <= N:
    row = str(count) * N
    print(row)
    count = count + 1
