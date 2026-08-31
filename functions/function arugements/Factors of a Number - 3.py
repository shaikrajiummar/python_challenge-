def factors_of_n(number):
    # complete this function
    factors_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors_list.append(str(i))
    return " ".join(factors_list)


number = int(input())
result = factors_of_n(number)  # call the factors_of_n function
print(result)