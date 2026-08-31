def get_even_numbers_count(numbers):
    # complete this function
    count = 0
    num_list = numbers.split()
    for num in num_list:
        if int(num) % 2 == 0:
            count += 1
    return count


numbers = input()
result = get_even_numbers_count(numbers)  # call the get_even_numbers_count function
print(result)