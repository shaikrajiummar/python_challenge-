# Read the number of inputs n
n = int(input())

# Read the first input and set it as the smallest initially
first = int(input())
small = first

# Loop n-1 times to read the rest of the inputs and find the smallest
for i in range(n - 1):
    num = int(input())
    if num < small:
        small = num

print(small)
