# Read the integer N
N = int(input())

# Print the top half of the number diamond
for i in range(1, N + 1):
    spaces = " " * (N - i)
    num = (str(i) + " ") * i
    print(spaces + num)

# Print the bottom half of the number diamond
for i in range(1, N):
    spaces = " " * i
    cuu = N - i
    num = (str(cuu) + " ") * cuu
    print(spaces + num)
