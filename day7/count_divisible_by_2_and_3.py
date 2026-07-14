# Read the integer N
N = int(input())

count = 0

# Loop from 1 to N and count numbers divisible by both 2 and 3 (i.e., divisible by 6)
for i in range(1, N + 1):
    if i % 2 == 0 and i % 3 == 0:
        count += 1

print(count)
