# Read the integer N
N = int(input())

sum = 0

# Loop up to N // 2 to find all proper divisors (factors excluding N itself)
for i in range(1, (N // 2) + 1):
    if N % i == 0:
        sum += i

# Check if the sum of proper divisors equals the original number N
if sum == N:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
