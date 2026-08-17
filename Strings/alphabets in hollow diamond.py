n = int(input())

# Upper half (including middle row)
for i in range(n):
    spaces = " " * (n - 1 - i)
    if i == 0:
        print(spaces + chr(65))
    else:
        left_char = chr(65 + (2 * i - 1))
        right_char = chr(65 + (2 * i))
        hollow_spaces = " " * (2 * i - 1)
        print(spaces + left_char + hollow_spaces + right_char)

# Lower half
for i in range(n - 2, -1, -1):
    spaces = " " * (n - 1 - i)
    if i == 0:
        print(spaces + chr(65))
    else:
        left_char = chr(65 + (2 * i - 1))
        right_char = chr(65 + (2 * i))
        hollow_spaces = " " * (2 * i - 1)
        print(spaces + left_char + hollow_spaces + right_char)