# Read the integer N
N = int(input())

# Loop from 1 to N and print all factors on the same line
for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=" ")
