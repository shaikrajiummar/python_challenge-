# Read the integer N
N = int(input())

# Solid Pyramid
for i in range(1, N + 1):
    spaces = " " * (N - i)
    stars = "* " * i
    print(spaces + stars)

# Hollow Inverted Pyramid
for i in range(N - 1, 0, -1):
    spaces = " " * (N - i)

    if i == 1:
        print(spaces + "*")
    else:
        inner_spaces = " " * (2 * i - 3)
        print(spaces + "*" + inner_spaces + "*")
