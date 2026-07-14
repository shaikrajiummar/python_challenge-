# Read the integer N
N = int(input())

# Loop backwards from N to 1 and print the inverted triangle pattern
for i in range(N, 0, -1):
    if i == N:
        print("* " * i)
    else:
        print("+ " * i)
