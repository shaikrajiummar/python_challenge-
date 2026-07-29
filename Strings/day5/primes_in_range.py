# Read range limits M and N
m = int(input())
n = int(input())

# Loop to find and print all prime numbers in the range [M, N]
for i in range(m, n + 1):
    if i > 1:
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            print(i)
