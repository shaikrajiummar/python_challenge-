# Read integers N and M
N = int(input())
M = int(input())

power = 1

# Multiply N by itself M times using a loop to calculate N^M
for i in range(M):
    power *= N

print(power)
