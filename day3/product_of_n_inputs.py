# Read the number of inputs N
N = int(input())

product = 1

# Loop N times to read values and calculate the product
for i in range(N):
    num = int(input())
    product = product * num

print(product)
