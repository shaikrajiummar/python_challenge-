# Read integers X and N
X = int(input())
N = int(input())

sum = 0

# Loop from 1 to N and calculate the alternating sum of odd powers of X
# (e.g. X^1 - X^3 + X^5 - X^7 + ...)
for i in range(1, N + 1):
    power = 2 * i - 1
    tern = X ** power
    if i % 2 == 0:
        sum -= tern
    else:
        sum += tern

print(sum)
