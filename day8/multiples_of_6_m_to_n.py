# Read integers M and N
M = int(input())
N = int(input())

count = 0
div = ""

# Loop from M to N and find numbers divisible by 6
for i in range(M, N + 1):
    if i % 6 == 0:
        count = count + 1
        div = div + str(i) + " "

# Check if any multiples of 6 were found
if count == 0:
    print("No Numbers Found")
else:
    print(div)
