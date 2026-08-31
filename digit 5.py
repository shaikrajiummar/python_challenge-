n = int(input())

for i in range(1, 2 * n):
    if i == 1 or i == n or i == 2 * n - 1:
        # Top, middle, and bottom horizontal lines
        print("* " * n)
    elif i < n:
        # Upper section: star aligned to the left
        print("* ")
    else:
        # Lower section: star aligned to the right
        print("  " * (n - 1) + "* ")