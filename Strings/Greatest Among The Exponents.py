a = int(input())
b = int(input())

result_1 = a ** b
result_2 = b ** a

if result_1 > result_2:
    print(result_1)
else:
    print(result_2)