n = int(input())

for _ in range(n):
    num = int(input())
    
    # Check if num is prime
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        # Print the first prime number and stop reading further inputs
        if is_prime:
            print(num)
            break