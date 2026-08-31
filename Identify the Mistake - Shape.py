n = int(input())
for i in range(0, n):
  row_out = " " * (n - 1 - i)
  row_out = row_out + "$" * n
  print(row_out)