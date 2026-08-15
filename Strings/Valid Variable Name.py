s = input()

is_valid = True

# First character cannot be a digit and must be a letter or underscore
first_char = s[0]
if not (first_char.isalpha() or first_char == "_"):
  is_valid = False
else:
  # Remaining characters must be letters, digits, or underscores
  for char in s[1:]:
    if not (char.isalnum() or char == "_"):
      is_valid = False
      break

print(is_valid)