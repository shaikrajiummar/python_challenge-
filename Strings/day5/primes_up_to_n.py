# Read upper limit N
n = int(input())

# Loop to find and print all prime numbers from 2 to N
for i in range(2, n + 1):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)
