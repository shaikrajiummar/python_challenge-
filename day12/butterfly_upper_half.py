# Read the integer N
N = int(input())

# Loop to print the upper half of the hollow butterfly with a solid bottom row
for i in range(1, N + 1):
    if i == N:
        print("* " * (2 * N))
    else:
        left_inner = " " * (2 * i - 3)
        middle_spaces = " " * (4 * (N - i) + 1)

        if i == 1:
            print("*" + middle_spaces + "*")
        else:
            print("*" + left_inner + "*" + middle_spaces + "*" + left_inner + "*")
