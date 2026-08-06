# Read upper limit N
n = int(input())
count = 0

# Loop to find Pythagorean triplets (A, B, C) where A < B < C <= N and A^2 + B^2 = C^2
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        for c in range(b + 1, n + 1):
            if a * a + b * b == c * c:
                count += 1

# Print the total count of valid triplets
print(count)
