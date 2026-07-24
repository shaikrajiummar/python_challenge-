# Read the input password
password = input()

ha_upper = False
# Check if there is at least one uppercase character in the password
for char in password:
    if char.isupper():
        ha_upper = True
        break

# Print the validation result
if ha_upper:
    print("Valid Password")
else:
    print("Invalid Password")
