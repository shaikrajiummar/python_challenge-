s = input()
result = ""
is_first_letter = True

for char in s:
    if char == " ":
        result += " "
        is_first_letter = True
    elif is_first_letter:
        result += chr(ord(char) + 1)
        is_first_letter = False
    else:
        result += char

print(result)