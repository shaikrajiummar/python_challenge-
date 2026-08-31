n = int(input())

for i in range(n):
  char = chr(65 + i)
  left_spaces = " " * (n - 1 - i)
  middle_spaces = " " * (2 * (n - 1 - i) + 1)

  if i == 0:
    print(left_spaces + char + middle_spaces + char)
  else:
    inner_spaces = " " * (2 * i - 1)
    half = char + inner_spaces + char
    print(left_spaces + half + middle_spaces + half)