# Read the base X and the number of terms N
X = int(input())
N = int(input())

sum_val = 0

# Loop from 1 to N to sum the even powers of X (X^2 + X^4 + ... + X^(2N))
for i in range(1, N + 1):
    csum = X ** (2 * i)
    sum_val = sum_val + csum

print(sum_val)
