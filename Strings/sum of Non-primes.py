n = int(input())

non_prime_sum = 0

for _ in range(n):
    num = int(input())
    
    # Check if the number is NOT prime
    if num <= 1:
        non_prime_sum += num
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if not is_prime:
            non_prime_sum += num

print(non_prime_sum)