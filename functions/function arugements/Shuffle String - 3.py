def shuffle_string(string, indexes_list):
    # complete this function
    shuffled_characters = []
    indices = indexes_list.split()
    for index in indices:
        shuffled_characters.append(string[int(index)])
    return "".join(shuffled_characters)


string = input()
indices_list = input()
result = shuffle_string(string, indices_list)  # call the shuffle_string function
print(result)