# Read the integer N
N = int(input())

# Loop from 0 to N-1 and print a right-aligned inverted star triangle
for i in range(N):
    spaces = "  " * i
    star = "* " * (N - i)
    print(spaces + star)
