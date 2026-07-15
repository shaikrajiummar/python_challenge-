# Read the integer N
N = int(input())

sum = 0

# Loop from 1 to N and sum the series of 2s (2 + 22 + 222 + ...)
for i in range(1, N + 1):
    series = int("2" * i)
    sum += series

print(sum)
