# Read the number of inputs N
N = int(input())

product = 1

# Loop N times, read an integer each time, and calculate cumulative product
for i in range(N):
    number = int(input())
    product = product * number

print(product)
