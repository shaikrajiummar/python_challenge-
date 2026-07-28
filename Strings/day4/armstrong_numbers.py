# Read the upper limit N
n = int(input())

# Loop to find and print all Armstrong numbers up to N
for i in range(1, n + 1):
    num_str = str(i)
    digits = len(num_str)
    digit_sum = 0
    
    for digit in num_str:
        digit_sum += int(digit) ** digits
        
    if digit_sum == i:
        print(i)
