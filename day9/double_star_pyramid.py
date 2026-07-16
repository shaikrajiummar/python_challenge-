# Read the integer N
N = int(input())

# Loop from 1 to N to print two pyramids side by side
for i in range(1, N + 1):
    spaces = " " * (N - i)
    star = "* " * i
    half = spaces + star
    row = half + spaces + half
    print(row)
