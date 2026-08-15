s = input()

smallest_char = s[0]

for char in s:
  if ord(char) < ord(smallest_char):
    smallest_char = char

print(smallest_char)