def check_is_prime(m, n):
    # complete this function
    primes = []
    for num in range(m, n + 1):
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(str(num))
    return " ".join(primes)


m = int(input())
n = int(input())
prime_numbers = check_is_prime(m, n)  # Call the check_is_prime function
print(prime_numbers)