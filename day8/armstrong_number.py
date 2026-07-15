# Read N as a string to easily count digits and iterate
N = input()

power = len(N)
sum = 0

# Loop through each digit and add digit^power to sum
for digit in N:
    sum += int(digit) ** power

# Check if the sum of powered digits equals the original number N
if sum == int(N):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
