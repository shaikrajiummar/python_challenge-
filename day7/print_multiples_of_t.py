# Read integers N and T
N = int(input())
T = int(input())

# Loop from 1 to N and print multiples of T
for i in range(1, N + 1):
    if i % T == 0:
        print(i)
