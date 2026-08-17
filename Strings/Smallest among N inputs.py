n = int(input())

smallest = int(input())
print(smallest)

for _ in range(n - 1):
    num = int(input())
    if num < smallest:
        smallest = num
    print(smallest)