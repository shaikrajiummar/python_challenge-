d = int(input())

if d <= 10:
    score = d
else:
    score = 10 + (d - 10) * 3

print(score)