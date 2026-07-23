# Read the input password
password = input()

upper = False
lower = False
digit = False

# Loop through each character to check character types
for char in password:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        digit = True

# Validate if password contains at least one uppercase, lowercase, and digit
if upper and lower and digit:
    print("Valid Password")
else:
    print("Invalid Password")
