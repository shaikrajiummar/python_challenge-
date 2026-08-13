m = int(input())
n = int(input())

odd_count = 0
even_count = 0

for i in range(m, n + 1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(odd_count)
print(even_count)