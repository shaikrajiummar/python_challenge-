# Read size N
n = int(input())
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Loop to print the alphabet grid pattern
for i in range(n):
    row = ""
    for j in range(n):
        row += alphabets[j] + " "
    print(row)
