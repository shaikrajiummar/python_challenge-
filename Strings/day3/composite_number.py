# Read the integer N
n = int(input())

factor = 0
# Loop to count all factors of N
for i in range(1, n + 1):
    if n % i == 0:
        factor += 1

# If factors count > 2, it is a composite number
composite = factor > 2
print(composite)
