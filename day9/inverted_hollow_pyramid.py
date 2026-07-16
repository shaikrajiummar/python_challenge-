# Read the integer N
N = int(input())

# Loop from 1 to N to print the inverted hollow pyramid pattern
for i in range(1, N + 1):
    if i == 1:
        print("* " * (2 * N - 1))
    else:
        lsapce = " " * (i - 1)
        star = "* " * (N - i + 1)
        mspaces = "  " * (i - 2)
        print(lsapce + star + mspaces + star)
