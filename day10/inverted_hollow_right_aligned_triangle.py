# Read the integer N
n = int(input())

# Loop from 1 to n to print the inverted hollow right-aligned star triangle
for i in range(1, n + 1):
    if i == 1:
        print("* " * n)
    elif i == n:
        print("  " * (n - 1) + "* ")
    else:
        lead = "  " * (i - 1)
        hollow = "  " * (n - i - 1)
        print(lead + "* " + hollow + "* ")
