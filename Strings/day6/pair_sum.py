# Read target sum N
n = int(input())

# Calculate count of unique pairs (A, B) where A < B and A + B = N
count = (n - 1) // 2

# Print the count
print(count)
