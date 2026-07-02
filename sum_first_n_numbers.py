# Read the integer N
N = int(input())

count = 0
current = 1

# Calculate the sum of the first N natural numbers using a while loop
while current <= N:
    count += current
    current += 1 
    
print(count)
