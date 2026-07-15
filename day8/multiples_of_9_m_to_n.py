# Read integers M and N
M = int(input())
N = int(input())

count = 0
div = ""

# Loop from M to N and find numbers divisible by 9
for num in range(M, N + 1):
    if num % 9 == 0:
        count = count + 1
        div = div + str(num) + " "

# Check if any multiples of 9 were found
if count == 0:
    print("No Numbers found")
else:
    print(div)
