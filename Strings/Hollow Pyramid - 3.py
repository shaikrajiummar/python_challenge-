n = int(input())

# Top half (including the widest row)
print("|")
for i in range(1, n):
    spaces = " " * i
    print(f"|{spaces}\\")

# Bottom half
for i in range(n - 1, 0, -1):
    spaces = " " * i
    print(f"|{spaces}/")
print("|")