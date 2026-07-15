# Read integers X and N
X = int(input())
N = int(input())

sum = 0

# Loop from 1 to N and sum the squares of repeated digit series
# For example, if X=2, N=3, it sums 2^2 + 22^2 + 222^2
for i in range(1, N + 1):
    value = int(str(X) * i) ** 2
    sum += value

print(sum)
