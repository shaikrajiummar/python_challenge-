# Read the number of inputs N
N = int(input())

# Read the first input and set it as the greatest initially
first = int(input())
greatest = first

# Loop N-1 times to read the rest of the inputs and find the greatest
for i in range(N - 1):
    num = int(input())
    if num > greatest:
        greatest = num

print(greatest)
