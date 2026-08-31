a = int(input())
b = int(input())
c = int(input())

d = (b**2 - 4 * a * c) ** 0.5

r1 = (-b + d) / (2 * a)
r2 = (-b - d) / (2 * a)

print(round(r1, 2))
print(round(r2, 2))