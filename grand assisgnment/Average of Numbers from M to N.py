m = int(input())
n = int(input())

total_sum = 0
count = (n - m) + 1

for num in range(m, n + 1):
  total_sum += num

average = total_sum / count

print(total_sum)
print(average)