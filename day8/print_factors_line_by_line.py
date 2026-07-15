# Read the integer N
N = int(input())

# Loop from 1 to N and print each factor on a new line
for i in range(1, N + 1):
    if N % i == 0:
        print(i)
