# Read the integer N
n = int(input())
digit = 0

# Loop from 1 to N and count the total number of digits
for i in range(1, n + 1):
    length = len(str(i))
    digit += length

print(digit)
