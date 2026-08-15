n = int(input())

# Upper half (including the middle row)
for i in range(n):
  char = chr(65 + i)
  left_spaces = " " * (n - 1 - i)
  if i == 0:
    print(left_spaces + char)
  else:
    hollow_spaces = " " * (2 * i - 1)
    print(left_spaces + char + hollow_spaces + char)

# Lower half
for i in range(n - 2, -1, -1):
  char = chr(65 + i)
  left_spaces = " " * (n - 1 - i)
  if i == 0:
    print(left_spaces + char)
  else:
    hollow_spaces = " " * (2 * i - 1)
    print(left_spaces + char + hollow_spaces + char)