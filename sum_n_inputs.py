# Read the number of inputs N
N = int(input())

count = 0
i = 0

# Loop N times to read values and add them to the total sum
while i < N:
    value = int(input())
    count = count + value
    i = i + 1

print(count)
