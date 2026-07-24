# Read the input integer as a string
N_str = input()

even_count = 0
# Loop through each digit in the input string
for char in N_str:
    if char.isdigit():
        digit = int(char)
        if digit % 2 == 0:
            even_count += 1

# Check if the count of even digits is greater than two
if even_count > 2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
