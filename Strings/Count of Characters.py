s = input()
n = int(input())

count = 0
for char in s:
  if ord(char) == n:
    count += 1

print(count)