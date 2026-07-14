# Read the integer N
N = int(input())

count = 0

# Loop from 1 to N and count numbers divisible by both 6 and 8 (i.e. divisible by 24)
for i in range(1, N + 1):
    if i % 6 == 0 and i % 8 == 0:
        count += 1

print(count)
