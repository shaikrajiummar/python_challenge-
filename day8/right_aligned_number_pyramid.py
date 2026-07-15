# Read the integer N
N = int(input())

# Loop from 1 to N and print a right-aligned number pyramid
for i in range(1, N + 1):
    spaces = "  " * (N - i)
    num = str(i) + " "
    numbers = num * ((2 * i) - 1)
    print(spaces + numbers)
