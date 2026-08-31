n = int(input())

last_digit_n = n % 10
square_n = n ** 2
last_digit_square = square_n % 10

if last_digit_n == last_digit_square:
    print("Equal")
else:
    print("Not Equal")