# Read input as string to find number of digits easily
num = input()
k = len(num)
sum = 0

# Loop through each digit, raise to power of k, and add to sum
for digit in num:
    sum += int(digit) ** k

print(sum)
