s = input()

is_valid = True

for char in s:
  # Check if each character is within 'a'-'z' or 'A'-'Z'
  if not (
      (ord("a") <= ord(char) <= ord("z")) or (ord("A") <= ord(char) <= ord("Z"))
  ):
    is_valid = False
    break

print(is_valid)