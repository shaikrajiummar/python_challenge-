n = int(input())

for i in range(1, n + 1):
    spaces = " " * (n - i)
    left_side = "".join(str(j) for j in range(i, 0, -1))
    right_side = "".join(str(j) for j in range(2, i + 1))
    print(spaces + left_side + right_side)