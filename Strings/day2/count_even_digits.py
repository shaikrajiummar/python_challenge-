N = input()

count = 0

for digit in N:
    if int(digit) % 2 == 0:
        count += 1

if count > 2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
