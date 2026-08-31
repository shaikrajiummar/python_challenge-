def get_first_upper_letter(string):
    # complete this function
    for char in string:
        if char.isupper():
            return char


string = input()
upper_case_character = get_first_upper_letter(string)  # call the get_first_upper_letter function
print(upper_case_character)