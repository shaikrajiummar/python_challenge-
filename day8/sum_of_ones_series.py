# Read the integer N
N = int(input())

sum = 0

# Loop from 1 to N and sum the series of 1s (1 + 11 + 111 + ...)
for i in range(1, N + 1):
    series = int("1" * i)
    sum += series

print(sum)
