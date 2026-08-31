n = int(input())

for i in range(n):
  char = chr(65 + i)
  outer_spaces = " " * i

  if i == 0:
    middle_spaces = " " * (2 * (n - 1) - 1)
    print(char + middle_spaces + char)
  else:
    inner_spaces = " " * (2 * i - 1)
    middle_spaces = " " * (2 * (n - 1 - i) - 1)

    left_half = char + inner_spaces + char
    right_half = char + inner_spaces + char

    if i == n - 1:
      print(outer_spaces + char + inner_spaces + char + inner_spaces + char)
    else:
      print(outer_spaces + left_half + middle_spaces + right_half)