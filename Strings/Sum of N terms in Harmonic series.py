n = int(input())

harmonic_sum = 0.0
for i in range(1, n + 1):
    harmonic_sum += 1 / i

print(round(harmonic_sum, 2))