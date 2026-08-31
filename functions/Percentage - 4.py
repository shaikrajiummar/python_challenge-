def calculate_percentage(number):
    # complete this function
    if number < 1000:
        return (5 / 100) * number
    else:
        return (10 / 100) * number


number = int(input())
result = calculate_percentage(number)  # Call the calculate_percentage function
print(result)