# Read the integer N
n = int(input())

# Loop from 1 to n to print the top half of the diamond of numbers
for i in range(1, n + 1):
    row = (str(i) + " ") * i
    print(row)

# Loop from n-1 down to 1 to print the bottom half of the diamond of numbers
for i in range(n - 1, 0, -1):
    row = (str(i) + " ") * i
    print(row)
