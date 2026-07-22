# Read dimensions M (rows) and N (columns)
M = int(input())
N = int(input())

# Loop to print the hollow rectangle of stars
for i in range(1, M + 1):
    if i == 1 or i == M:
        print("* " * N)
    else:
        left_star = "* "
        rigjt = "* "
        holl = " " * (2 * (N - 2))
        print(left_star + holl + rigjt)
