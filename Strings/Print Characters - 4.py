s = input()
m = int(input())
n = int(input())

for char in s:
    if m <= ord(char) <= n:
        print(char, end=" ")