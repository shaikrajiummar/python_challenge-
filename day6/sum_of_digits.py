# Read string N (representing a number)
N = input()

total = 0

# Loop through each digit in the string N, convert to integer, and add to total
for i in N:
    total = total + int(i)

print(total)
