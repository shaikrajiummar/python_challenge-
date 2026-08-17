n = int(input())

# Top half
for i in range(n):
    spaces = " " * (n - 1 - i)
    inner_spaces = " " * (2 * i)
    print(spaces + "/" + inner_spaces + "\\")

# Bottom half
for i in range(n):
    spaces = " " * i
    inner_spaces = " " * (2 * (n - 1 - i))
    print(spaces + "\\" + inner_spaces + "/")