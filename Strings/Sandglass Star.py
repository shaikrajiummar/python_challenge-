n = int(input())

# Top inverted pyramid (from n down to 1 stars)
for i in range(n, 0, -1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)

# Bottom upright pyramid (from 2 up to n stars)
for i in range(2, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)