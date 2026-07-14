# Read integers T, M, and N
T = int(input())
M = int(input())
N = int(input())

sum = 0

# Loop from M to N and sum all numbers divisible by T
for i in range(M, N + 1):
    if i % T == 0:
        sum += i

print(sum)
