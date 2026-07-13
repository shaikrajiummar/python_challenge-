# Read the integer N
N = int(input())

fact = 1

# Loop and calculate the factorial of N
for i in range(1, N + 1):
    fact *= i

print(fact)
