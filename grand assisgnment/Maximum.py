n = int(input())

current_max = int(input())
print(current_max)

for _ in range(n - 1):
    num = int(input())
    if num > current_max:
        current_max = num
    print(current_max)