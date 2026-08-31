def fizz_buzz(number):
    # Complete this function
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


number = int(input())
# Call the fizz_buzz function
result = fizz_buzz(number)
print(result)