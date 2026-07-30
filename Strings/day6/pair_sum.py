# Read target sum N
n = int(input())
count = 0

# Loop through all possible values of A
for a in range(1, n + 1):
    # Calculate what B must be for the sum to equal N
    b = n - a
    
    # Check if the condition A < B is satisfied
    if a < b:
        count += 1
    else:
        # Since A keeps increasing, once A >= B, it will always be true. 
        # We can break early to save time.
        break

# Print the total count of valid pairs
print(count)
