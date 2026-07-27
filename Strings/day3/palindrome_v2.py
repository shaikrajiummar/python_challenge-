# Read the input string
input_str = input()

# Convert the string to lowercase
palindrome = input_str.lower()

# Remove spaces, single quotes, and double quotes
palindrome = palindrome.replace(" ", "")
palindrome = palindrome.replace("'", "")
palindrome = palindrome.replace('"', "")

# Reverse the cleaned string
reverse = palindrome[::-1]

# Print whether the cleaned string is a palindrome (True/False)
print(palindrome == reverse)
