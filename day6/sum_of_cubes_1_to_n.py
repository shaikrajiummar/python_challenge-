# Read the integer N
N = int(input())

sum = 0
product = 0

# Loop and calculate the sum of cubes from 1 to N
# Note: Variable 'product' is defined but unused.
for i in range(1, N + 1):
    sum += i ** 3

print(sum)
