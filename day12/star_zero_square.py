# Read the size of the square N
N = int(input())

# Loop to print the star-bordered square filled with zeros
for i in range(1, N + 1):
    if i == 1 or i == N:
        print("* " * N)
    else:
        print("* " + "0 " * (N - 2) + "* ")
