# Read the integer N
N = int(input())

# Loop backwards from N to 1 and print an inverted triangle of stars
for i in range(N, 0, -1):
    print("* " * i)
