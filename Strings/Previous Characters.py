s = input()

for char in s:
  if char != " ":
    prev_char = chr(ord(char) - 1)
    print(prev_char)