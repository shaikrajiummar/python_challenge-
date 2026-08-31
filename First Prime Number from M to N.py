m = int(input())
n = int(input())

found_prime = False

for num in range(m, n + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num)
            found_prime = True
            break

if not found_prime:
    print("No prime numbers in the given range")