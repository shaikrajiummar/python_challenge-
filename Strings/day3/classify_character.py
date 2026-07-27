# Read the input character
c = input()

# Classify the character type
if c.isdigit():
    print("Digit")
elif c.islower():
    print("Lowercase Letter")
elif c.isupper():
    print("Uppercase Letter")
else:
    print("Special Charater")
