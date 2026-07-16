# Read the integer N
N = int(input())

# Loop from 1 to N to print the top part of the butterfly pattern
for i in range(1, N + 1):
    spaces = 4 * (N - i)
    star = i
    row = "* " * star + " " * spaces + "* " * star
    print(row)
