def is_prime(number):
    # complete this function
    if number <= 1:
        return "Not a Prime Number"
    for i in range(2, number):
        if number % i == 0:
            return "Not a Prime Number"
    return "Prime Number"


number = int(input())
result = is_prime(number)  # call is_prime function
print(result)