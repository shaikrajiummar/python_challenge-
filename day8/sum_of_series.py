# Read input X as string and N as integer
X = input()
N = int(input())

sum = 0

# Loop from 1 to N and sum the series (X + XX + XXX + ...)
for i in range(1, N + 1):
    value = int(X * i)
    sum += value

print(sum)
