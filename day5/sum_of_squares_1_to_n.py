# Read the integer N
N = int(input())

sum = 0

# Loop and calculate the sum of squares of numbers from 1 to N
for i in range(1, N + 1):
    sum = sum + (i ** 2)

print(sum)
