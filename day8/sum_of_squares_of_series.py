# Read input X as a string and N as an integer
X = input()
N = int(input())

sum = 0

# Loop from 1 to N and sum the squares of repeated string values converted to integers
for i in range(1, N + 1):
    value = int(X * i) ** 2
    sum += value

print(sum)
