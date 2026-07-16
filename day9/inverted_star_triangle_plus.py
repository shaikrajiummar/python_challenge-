# Read the integer N
N = int(input())

# Print the top row of plus (+) characters
print("+ " * N)

# Loop from 1 to N-1 to print the inverted star triangle
for i in range(1, N):
    spaces = " " * i
    star = "* " * (N - i)
    print(spaces + star)
