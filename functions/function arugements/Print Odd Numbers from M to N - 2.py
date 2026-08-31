def get_odd_numbers_in_range(start_number, end_number):
    # complete this function
    odd_list = []
    for i in range(start_number, end_number + 1):
        if i % 2 != 0:
            odd_list.append(str(i))
    return " ".join(odd_list)


start_number = int(input())
end_number = int(input())
odd_numbers = get_odd_numbers_in_range(start_number, end_number)  # Call the get_odd_numbers_in_range function
print(odd_numbers)