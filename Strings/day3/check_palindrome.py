# Read the input string
input_str = input()

# Convert the string to lowercase for case-insensitive check
lower = input_str.lower()
reverse = lower[::-1]

# Print if the string is a palindrome
if lower == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
