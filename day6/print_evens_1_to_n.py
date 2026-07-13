# Read the integer N
N = int(input())

# Loop from 1 to N and print all even numbers (each on a new line)
for i in range(1, N + 1):
    if i % 2 == 0:
        print(i)
