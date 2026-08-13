m = int(input())
n = int(input())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
curr_idx = 0

for i in range(m):
    row = ""
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            # Border cells: append the alphabet character with a space
            row += alphabets[curr_idx] + " "
        else:
            # Inner hollow cells: append two spaces
            row += "  "
        curr_idx += 1
    print(row)