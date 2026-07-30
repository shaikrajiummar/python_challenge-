# Read the target sum N
n = int(input())
count = 0

# Loop to find triplets (A, B, C) where A < B < C and A + B + C = N
for a in range(1, n + 1):
    # Loop through values of B starting from a + 1 to maintain A < B
    for b in range(a + 1, n + 1):
        # Calculate C based on the remaining sum
        c = n - (a + b)
        
        # Check if C satisfies B < C
        if b < c:
            count += 1
        else:
            # Since B is increasing, C will only decrease; break early
            break

# Print the total count of valid triplets
print(count)
