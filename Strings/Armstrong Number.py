n = int(input())

# Extract individual digits using math operations
digit3 = n % 10
digit2 = (n // 10) % 10
digit1 = n // 100

# Sum of cubes
sum_of_cubes = (digit1 ** 3) + (digit2 ** 3) + (digit3 ** 3)

# Print result
print(sum_of_cubes == n)