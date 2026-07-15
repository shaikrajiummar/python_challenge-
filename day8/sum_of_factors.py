# Read the integer N
N = int(input())

sum = 0

# Loop from 1 to N and sum all factors of N (numbers that divide N perfectly)
for i in range(1, N + 1):
    if N % i == 0:
        sum += i

print(sum)
