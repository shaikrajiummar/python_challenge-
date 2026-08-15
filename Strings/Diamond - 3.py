n = int(input())

# Upper half (including middle row)
for i in range(1, n + 1):
  dots = ". " * (n - i)
  zeros = "0 " * (2 * i - 1)
  row = dots + zeros + dots
  print(row.strip())

# Lower half
for i in range(n - 1, 0, -1):
  dots = ". " * (n - i)
  zeros = "0 " * (2 * i - 1)
  row = dots + zeros + dots
  print(row.strip())