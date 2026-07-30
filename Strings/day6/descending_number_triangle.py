# Read starting number S and size N
s = int(input())
n = int(input())

# Calculate total numbers in the triangle (K) using arithmetic progression sum
k = (n * (n + 1)) // 2

# Define the starting number as K + S - 1
current_number = k + s - 1

# Loop to print the right-angled triangle of descending numbers
for i in range(1, n + 1):
    row_output = ""
    # Each row 'i' prints exactly 'i' numbers
    for j in range(i):
        row_output += str(current_number) + " "
        current_number -= 1
    print(row_output)
