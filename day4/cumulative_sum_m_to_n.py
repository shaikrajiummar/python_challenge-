# Read integers M and N
M = int(input())
N = int(input())

sum = 0

# Loop from M to N and print the running sum at each step
for i in range(M, N + 1):
    sum += i
    print(sum)
