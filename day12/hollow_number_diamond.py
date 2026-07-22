# Read the integer N
N = int(input())

# Loop to print the top half of the hollow number diamond
for i in range(1, N + 1):
    leading_spaces = " " * (2 * (N - i))
    if i == 1:
        print(leading_spaces + str(i))
    else:
        hollow_spaces = " " * (2 * i - 3)
        print(leading_spaces + str(i) + hollow_spaces + str(i))

# Loop to print the bottom half of the hollow number diamond
for i in range(N - 1, 0, -1):
    leading_spaces = " " * (2 * (N - i))
    if i == 1:
        print(leading_spaces + str(i))
    else:
        hollow_spaces = " " * (2 * i - 3)
        print(leading_spaces + str(i) + hollow_spaces + str(i))
