# Read integers x and n
x = int(input())
n = int(input())

sum = 0

# Loop from 1 to n and calculate the alternating sum of even powers of x
# (e.g. x^2 - x^4 + x^6 - x^8 + ...)
for i in range(1, n + 1):
    power = 2 * i
    value = x ** power
    if i % 2 != 0:
        sum += value
    else:
        sum -= value

print(sum)
