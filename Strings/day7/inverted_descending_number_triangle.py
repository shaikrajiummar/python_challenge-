# Read starting number S and size N
s = int(input())
n = int(input())

k = n * (n + 1) // 2
num = k + s - 1

# Loop to print the inverted descending number triangle
for i in range(n, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num -= 1
    print()
