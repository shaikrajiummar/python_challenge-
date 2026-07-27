# Read grid dimensions M (rows) and N (columns)
m = int(input())
n = int(input())

# Construct boundary and middle rows
bound = "+" + ("-" * n) + "+"
middle = "|" + (" " * n) + "|"

# Print top boundary
print(bound)

# Print middle rows
for i in range(m):
    print(middle)

# Print bottom boundary
print(bound)
