# Read range limits A and B
a = int(input())
b = int(input())

# Loop to find and print all composite numbers in the range [A, B]
for i in range(a, b + 1):
    factor_count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            factor_count += 1
    # A composite number has more than 2 factors
    if factor_count > 2:
        print(i)
