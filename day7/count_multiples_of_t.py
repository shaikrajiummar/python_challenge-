# Read integers N and T
N = int(input())
T = int(input())

count = 0

# Loop from 1 to N and count multiples of T
for i in range(1, N + 1):
    if i % T == 0:
        count += 1

print(count)
