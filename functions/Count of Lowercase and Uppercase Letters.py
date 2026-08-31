def count_of_lowercase_and_uppercase_letters(arg_1):
    # Complete this function
    count_of_uppercase = 0
    count_of_lowercase = 0

    for char in arg_1:
        if char.isupper():
            count_of_uppercase += 1
        elif char.islower():
            count_of_lowercase += 1

    print(count_of_uppercase)
    print(count_of_lowercase)


word = input()
# Call the count_of_lowercase_and_uppercase_letters function
count_of_lowercase_and_uppercase_letters(word)