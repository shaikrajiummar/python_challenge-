# Read the input text
text = input()

reverse = " "

# Loop through each character and prepend it to build the reversed string
for char in text:
    reverse = char + reverse

print(reverse)
