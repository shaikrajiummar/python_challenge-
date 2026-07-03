# Read the integer N
N = int(input())

# Loop and print N - 1 rows of stars
for i in range(1, N):
    print("* " * i)

# Print a final row of N pluses at the bottom
print("+ " * N)
