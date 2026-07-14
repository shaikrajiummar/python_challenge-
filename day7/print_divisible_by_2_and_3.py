# Read the integer N
N = int(input())

# Loop from 1 to N and print numbers divisible by both 2 and 3 (i.e. multiples of 6)
for i in range(1, N + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
