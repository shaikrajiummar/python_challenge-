# Read the integer N
N = int(input())

# Print upper triangle of the diamond
for i in range(1, N + 1):
    spaces = " " * (N - i)
    star = "* " * i
    print(spaces + star)

# Print lower inverted triangle of the diamond
for i in range(1, N):
    spaces = " " * i
    star = "* " * (N - i)
    print(spaces + star)
