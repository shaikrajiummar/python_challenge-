# Read the integer N
N = int(input())

product = 1

# Loop from 1 to 10 and print the multiplication table row by row
for i in range(1, 11):
    print(N, "x", i, "=", N * i)
