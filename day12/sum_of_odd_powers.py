# Read the base X and the number of terms N
X = int(input())
N = int(input())

sum_val = 0

# Loop N times to sum the odd powers of X (X^1 + X^3 + ... + X^(2N-1))
for i in range(N):
    power = 2 * i + 1
    csum = X ** power
    sum_val = sum_val + csum

print(sum_val)
