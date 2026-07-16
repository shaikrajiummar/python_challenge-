# Read the integer N
N = int(input())

sum = 0
# Loop from 1 to N and print centered numbers pyramid
for i in range(1, N + 1):
    spaces = " " * (N - i)
    numbers = (str(i) + " ") * i
    print(spaces + numbers)
