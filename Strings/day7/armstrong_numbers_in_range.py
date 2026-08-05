# Read range limits M and N
m = int(input())
n = int(input())

count = 0

# Loop to find and print all Armstrong numbers in the range [M, N]
for i in range(m, n + 1):
    num = i
    power = len(str(i))
    total = 0

    while num != 0:
        digit = num % 10
        total += digit ** power
        num //= 10

    if total == i:
        print(i, end=" ")
        count += 1

# If no Armstrong numbers were found, print -1
if count == 0:
    print(-1)
