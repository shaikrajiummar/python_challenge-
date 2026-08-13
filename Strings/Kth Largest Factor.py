n = int(input())
k = int(input())

count = 0
kth_factor = None

# Iterate backwards from N down to 1 to find factors in descending order
for i in range(n, 0, -1):
    if n % i == 0:
        count += 1
        if count == k:
            kth_factor = i
            break

if kth_factor is not None:
    print(kth_factor)