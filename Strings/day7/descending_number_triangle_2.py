# Read starting number N and row count K
n = int(input())
k = int(input())

total = k * (k + 1) // 2
num = n + total - 1

# Loop to print the right-angled triangle of descending numbers
for i in range(1, k + 1):
    for j in range(i):
        print(num, end=" ")
        num -= 1
    print()
