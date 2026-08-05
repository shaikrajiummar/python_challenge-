# Read upper limit N
n = int(input())
count = 0

# Loop to count numbers not divisible by any number in range [2, 10]
for i in range(1, n + 1):
    if (i % 2 != 0 and i % 3 != 0 and i % 4 != 0 and
        i % 5 != 0 and i % 6 != 0 and i % 7 != 0 and
        i % 8 != 0 and i % 9 != 0 and i % 10 != 0):
        count += 1

# Print the final count
print(count)
