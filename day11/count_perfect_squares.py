# Read two integers A and B
A = int(input())
B = int(input())

count = 0

# Loop from A to B and count all perfect squares
for i in range(A, B + 1):
    root = int(i ** 0.5)
    if root * root == i:
        count += 1

print(count)
