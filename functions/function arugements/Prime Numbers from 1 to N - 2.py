def is_prime(number):
    # complete this function
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


n = int(input())
for i in range(1, n + 1):
    is_prime_number = is_prime(i)  # call the is_prime function
    if is_prime_number:
        print(i)