n = int(input())

for i in range(n):
    number = int(input())
    
    digits = str(number)
    power = len(digits)
    
    total = 0
    
    for digit in digits:
        total += int(digit) ** power
    
    if total == number:
        print(number)
