# Read the size parameter N
N = int(input())

# Loop to print the star-bordered rectangle filled with N-1 zeros in the middle
for i in range(1, N + 1):
    if i == 1 or i == N:
        print("* " * N)
    else:
        print("* " + "0 " * (N - 1) + "* ")
