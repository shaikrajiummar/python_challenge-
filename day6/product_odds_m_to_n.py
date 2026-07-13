# Read integers M and N
M = int(input())
N = int(input())

product = 1
odd = False

# Loop from M to N and calculate the product of odd numbers
for i in range(M, N + 1):
    if i % 2 != 0:
        product *= i
        odd = True

# If there were no odd numbers in the range, print 0
if not odd:
    product = 0

print(product)
