# Read integers N and K
N = int(input())
K = int(input())

sum = 0

# Loop from 1 to N and sum the Kth power of each integer i
for i in range(1, N + 1):
    sum += (i ** K)

print(sum)
