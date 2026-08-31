n = int(input())

cumulative_sum = 0
for i in range(1, n + 1):
    num = int(input())
    cumulative_sum += num
    avg = cumulative_sum / i
    print(round(avg, 3))