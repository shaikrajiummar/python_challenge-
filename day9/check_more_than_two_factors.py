# Read the integer N
N = int(input())
count = 0

# Loop from 1 to N to find and count the factors of N
for i in range(1, N + 1):
    if N % i == 0:
        count += 1

# Check if the number has strictly more than 2 factors
if count > 2:
    print("Number has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors")
