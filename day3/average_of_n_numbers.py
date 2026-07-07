# Read the integer N
N = int(input())

sum = 0

# Loop from 1 to N and calculate the sum
for i in range(1, N + 1):
    sum = sum + i

# Calculate and print the average
avg = sum / N
print(avg)
