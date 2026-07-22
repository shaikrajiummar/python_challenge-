# Read dimensions M (rows) and N (columns)
M = int(input())
N = int(input())

# Loop M times and print a row of N stars without space separators
for i in range(M):
    print("*" * N)
