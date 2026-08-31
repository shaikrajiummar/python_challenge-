def compare_numbers(first_number, second_number):
    # complete this function
    return first_number > 100 and second_number > 100 and first_number < second_number


first_number = int(input())
second_number = int(input())
is_true = compare_numbers(first_number, second_number)  # Call the compare_numbers function
print(is_true)