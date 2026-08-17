s = input()

result = ""
for char in s:
    if "a" <= char <= "y":
        result += chr(ord(char) + 1)
    elif char == "z":
        result += "a"
    elif "A" <= char <= "Y":
        result += chr(ord(char) + 1)
    elif char == "Z":
        result += "A"
    else:
        result += char

print(result)