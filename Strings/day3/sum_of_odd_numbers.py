# Read the integer N
n = int(input())

odd_sum = 0

# Loop to sum all odd numbers from 1 to N
for i in range(1, n + 1):
    if i % 2 != 0:
        odd_sum += i

# Print the final sum
print(odd_sum)
