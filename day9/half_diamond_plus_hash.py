# Read the integer N
N = int(input())

# Loop from 1 to N to print the top half of the diamond
for i in range(1, N + 1):
    spaces = "  " * (N - i)
    plus = "+ " * (i - 1)
    print(spaces + plus + "# ")

# Loop from 1 to N-1 to print the bottom half of the diamond
for i in range(1, N):
    spaces = "  " * i
    plus = "+ " * (N - i - 1)
    print(spaces + plus + "# ")
