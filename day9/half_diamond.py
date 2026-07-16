# Read the integer N
N = int(input())

# Loop from 1 to N to print the top half of the diamond
for i in range(1, N + 1):
    spaces = " " * (N - i)
    row = 2 * N - 1
    star = "* " * i
    print(star)

# Loop from 1 to N to print the bottom half of the diamond
for i in range(1, N + 1):
    spaces = " " * i
    star = "* " * (N - i)
    print(star)
