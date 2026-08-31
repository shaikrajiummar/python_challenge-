n = int(input())

for i in range(1, n + 1):
    row_str = ""
    for j in range(i):
        row_str += chr(65 + j) + " "
    print(row_str)