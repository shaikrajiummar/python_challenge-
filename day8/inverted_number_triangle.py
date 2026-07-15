# Read the integer N
N = int(input())

# Loop from 1 to N and print the inverted, right-aligned number triangle
for i in range(1, N + 1):
    num = (N + 1) - i
    spaces = " " * (i - 1)
    print(spaces + str(num) * num)
