n = int(input())
k = int(input())

count = 0
kth_factor = 1  # Default to 1 if fewer than K factors exist

# Iterate downwards from N to 1 to check factors in descending order
for i in range(n, 0, -1):
    if n % i == 0:
        count += 1
        if count == k:
            kth_factor = i
            break

print(kth_factor)