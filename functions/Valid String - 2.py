def valid_string(string):
    # complete this function
    if string[0].isdigit() or len(string) >= 6:
        return "Valid String"
    else:
        return "Invalid String"


string = input()
result = valid_string(string)  # Call the valid_string function
print(result)