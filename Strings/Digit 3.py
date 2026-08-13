n = int(input())

for i in range(1, 2 * n):
    if i == 1 or i == n or i == 2 * n - 1:
        # Top, middle, and bottom horizontal lines: N stars with spaces
        print("* " * n)
    else:
        # Vertical sections: right-aligned star with spaces before it
        print("  " * (n - 1) + "* ")