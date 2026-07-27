# Read the integer N
n = int(input())

even_sum = 0

# Loop to sum all even numbers from 1 to N
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i

# Print the final sum
print(even_sum)
