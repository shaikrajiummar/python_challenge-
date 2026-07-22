# Read the number of inputs N
N = int(input())

sum_val = 0

# Loop N times, read an integer, and add to sum_val
for i in range(1, N + 1):
    num = int(input())
    sum_val = sum_val + num

print(sum_val)
