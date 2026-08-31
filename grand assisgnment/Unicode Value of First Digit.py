s = input()

for char in s:
    if char.isdigit():
        print(ord(char))
        break