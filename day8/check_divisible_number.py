# Read the integer N
N = int(input())

divisible = False

# Loop from 2 to 9 and check if N is divisible by any of these numbers
for i in range(2, 10):
    if N % i == 0:
        divisible = True
        break

# Print the result based on divisibility
if divisible:
    print("Divisible Number")
else:
    print("Indivisible Number")
