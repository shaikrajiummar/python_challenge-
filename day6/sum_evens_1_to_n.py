# Read the integer N
N = int(input())

sum = 0

# Loop from 1 to N and sum all even numbers
for i in range(1, N + 1):
    if i % 2 == 0:
        sum += i

# Print the final sum
print(sum)
