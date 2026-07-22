# Read the starting integer M and the count N
M = int(input())
N = int(input())

sum_val = 0

# Loop N times to calculate sum of N consecutive integers starting from M
for i in range(N):
    num = M + i
    sum_val = sum_val + num

print(sum_val)
