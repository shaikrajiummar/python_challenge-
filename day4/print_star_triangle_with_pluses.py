# Read the integer N
N = int(input())

# Loop and print a star triangle of height N - 1 using nested loops
for i in range(1, N):
    for j in range(i):
        print("*", end=" ")
    print()

# Print N pluses at the bottom
for i in range(N):
    print("+", end=" ")
