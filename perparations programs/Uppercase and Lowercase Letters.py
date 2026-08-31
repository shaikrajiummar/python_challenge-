def get_lower_and_upper_case_letters(word):
    # Complete this function
    upper_case = ""
    lower_case = ""
    for char in word:
        if char.isupper():
            upper_case += char
        elif char.islower():
            lower_case += char

    print(upper_case)
    print(lower_case)


word = input()
# Call the get_lower_and_upper_case_letters function
get_lower_and_upper_case_letters(word)