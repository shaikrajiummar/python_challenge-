m = int(input())
n = int(input())

# The LCM will be at least equal to the larger of the two numbers
lcm = max(m, n)

while True:
    if lcm % m == 0 and lcm % n == 0:
        break
    lcm += 1

print(lcm)